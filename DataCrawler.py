import requests
import json
from selenium.webdriver import Chrome, ChromeOptions
from datastore import *
import time

class DataCrawler:
    def __gethistory(self):
        """
        得到历史数据，数据格式
        '20200820': {'confirm': 90053, 'heal': 84122, 'dead': 4716, 'importedCase': 2368, 'noInfect': 353,
        'nowConfirm': 1215, 'confirm_add': 40, 'heal_add': 95, 'dead_add': 3, 'importedCase_add': 22,
         'noInfect_add': 23, 'nowConfirm_add': -58}
        :return:  history ：字典
        """
        string = requests.get("https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list"
                              "?modules=chinaDayList,chinaDayAddList,cityStatis,nowConfirmStatis,provinceCompare")
        data_dict = json.loads(string.text)['data']
        history = {}

        for di in data_dict['chinaDayList']:
            date = '2020' + di['date'].replace('.', '')
            history[date] = {'confirm': di['confirm'],
                             'heal': di['heal'],
                             'dead': di['dead'],
                             'importedCase': di['importedCase'],
                             'noInfect': di['noInfect'],
                             'nowConfirm': di['nowConfirm']}

        for di in data_dict['chinaDayAddList']:
            date = '2020' + di['date'].replace('.', '')
            history[date].update(
                {'confirm_add': di['confirm'],
                 'heal_add': di['heal'],
                 'dead_add': di['dead'],
                 'importedCase_add': di['importedCase'],
                 'noInfect_add': di['infect'],
                 'nowConfirm_add': di['confirm'] - di['heal'] - di['dead']})

        return history

    def __getdetails(self):
        """
        得到每天的详细数据,数据格式
         ['2020-08-21 15:15:25', '新疆', '乌鲁木齐', 274, 845, 571, 0]
        :return: details ： 列表
        """
        string = requests.get("https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5")
        data_dict = json.loads(json.loads(string.text)["data"])

        update_time = data_dict["lastUpdateTime"]
        prov_city_details = data_dict["areaTree"][0]["children"]
        details = []

        for prov in prov_city_details:
            province = prov["name"]
            for cities in prov["children"]:
                city = cities["name"]
                nowConfirm = cities["total"]["nowConfirm"]
                confirm = cities["total"]["confirm"]
                heal = cities["total"]["heal"]
                dead = cities["total"]["dead"]
                details.append([update_time, province, city, nowConfirm, confirm, heal, dead])

        return details

    def insert_history(self):
        """
        插入初始数据到history
        """
        history = self.__getHistory()

        for k, v in history.items():
            db.session.add(History(time=k, confirm=v.get("confirm"), confirm_add=v.get("confirm_add"),
                                   heal=v.get("heal"), heal_add=v.get("heal_add"), dead=v.get("dead"),
                                   dead_add=v.get("dead_add"), nowConfirm=v.get("nowConfirm"),
                                   nowConfirm_add=v.get("nowConfirm_add"), noInfect=v.get("noInfect"),
                                   noInfect_add=v.get("noInfect_add"), importedCase=v.get("importedCase"),
                                   importedCase_add=v.get("importedCase_add")))

        db.session.commit()

    def update_history(self):
        """
        更新history，将新的数据插入到history
        :return:
        """
        history = self.__gethistory()
        history = sorted(history.items(), key=lambda x: x[0], reverse=True)

        for hi in history:
            v = hi[1]
            if not History.query.filter_by(time=hi[0]).first():
                db.session.add(History(time=hi[0], confirm=v.get("confirm"), confirm_add=v.get("confirm_add"),
                                       heal=v.get("heal"), heal_add=v.get("heal_add"), dead=v.get("dead"),
                                       dead_add=v.get("dead_add"), nowConfirm=v.get("nowConfirm"),
                                       nowConfirm_add=v.get("nowConfirm_add"), noInfect=v.get("noInfect"),
                                       noInfect_add=v.get("noInfect_add"), importedCase=v.get("importedCase"),
                                       importedCase_add=v.get("importedCase_add")))
            else:
                break

        db.session.commit()

    def update_details(self):
        details = self.__getdetails()

        if not Details.query.filter_by(update_time=details[0][0]).first():
            for di in details:
                db.session.add(Details(update_time=di[0], province=di[1], city=di[2],
                                       nowConfirm=di[3], confirm=di[4], heal=di[5], dead=di[6]))

            db.session.commit()

            ret = Details.query.filter(Details.update_time != details[0][0]).all()
            for ri in ret:
                db.session.delete(Details.query.get(ri.id))
            db.session.commit()

    def update_province(self):
        option = ChromeOptions()
        option.add_argument("headless")
        chrome = Chrome(options=option)
        chrome.get("https://news.qq.com/zt2020/page/feiyan.htm#/?nojump=1")
        update_time = chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/p/span")
        province = chrome.find_elements_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/table[2]/tbody/tr[1]/th/p[1]/span")
        nowConfirm = chrome.find_elements_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/table[2]/tbody/tr[1]/td[1]/p[1]")
        confirm = chrome.find_elements_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/table[2]/tbody/tr[1]/td[2]/p[1]")

        if not Province.query.filter_by(update_time=update_time.text).first():
            for i in range(len(province)):
                db.session.add(Province(update_time=update_time.text, province=province[i].text,
                                        nowConfirm=int(nowConfirm[i].text), confirm=int(confirm[i].text)))

            db.session.commit()

            ret = Province.query.filter(Province.update_time != update_time.text).all()
            for ri in ret:
                db.session.delete(Province.query.get(ri.id))
            db.session.commit()

    def province_history(self):
        string = requests.get("https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish")
        data = json.loads(string.text)["data"]
        province = []
        time = data[0]["trend"]["updateDate"]
        confirm = []
        data = data[:-2]

        for di in data:
            if di["name"] == "台湾":
                continue

            province.append(di["name"])
            confirm.append(di["trend"]["list"][1]["data"])

        print(province[-5])
        for i in range(32):
            print(len(confirm[i]))

        # for i in range(len(time)):
        #     for j in range(len(province)):
        #         t = "2020-" + time[i].replace('.', '-')
        #         # db.session.add(ProvinceHistory(time=t, province=province[j], confirm=confirm[j][i]))
        #         print(t, province[j], confirm[j][i])




if __name__ == '__main__':
    dc = DataCrawler()
    # dc.insertHistory()
    # dc.updateHistory()
    # dc.update_details()
    # dc.update_province()
    dc.province_history()