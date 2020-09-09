from flask import Flask, render_template, jsonify, flash, url_for, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
import cal
import time
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from datastore import *


@app.route("/time")
def get_time():
    time_str = time.strftime("%Y-%m-%d %X")
    return time_str


@app.route("/c1")
def getC1():
    ret = db.session.query(History.confirm, History.confirm_add,
                           History.heal, History.heal_add,
                           History.dead, History.dead_add).filter().order_by(History.time.desc()).first()

    return jsonify({"confirm": ret[0], "confirm_add": ret[1] if ret[1] <= 0 else "+" + str(ret[1]),
                    "heal": ret[2], "heal_add": ret[3] if ret[3] <= 0 else "+" + str(ret[3]),
                    "dead": ret[4], "dead_add": ret[5] if ret[5] <= 0 else "+" + str(ret[5])
                    })


@app.route("/c2")
def getC2():
    ret = db.session.query(History.nowConfirm, History.nowConfirm_add,
                           History.noInfect, History.noInfect_add,
                           History.importedCase, History.importedCase_add).filter().order_by(
        History.time.desc()).first()

    return jsonify({"nowConfirm": ret[0], "nowConfirm_add": ret[1] if ret[1] <= 0 else "+" + str(ret[1]),
                    "noInfect": ret[2], "noInfect_add": ret[3] if ret[3] <= 0 else "+" + str(ret[3]),
                    "importedCase": ret[4], "importedCase_add": ret[5] if ret[5] <= 0 else "+" + str(ret[5])
                    })


@app.route("/c3")
def getC3():
    ret = db.session.query(Province.province, Province.confirm).all()

    res = []
    for ri in ret:
        res.append({"name": ri[0], "value": int(ri[1])})

    return jsonify({"res": res})


@app.route("/l1")
def getL1():
    ret = db.session.query(History.time, History.nowConfirm, History.confirm,
                           History.heal, History.dead).all()
    ret = ret[7:]

    day, nowConfirm, confirm, heal, dead = [], [], [], [], []

    for ri in ret:
        day.append(ri[0].strftime("%m-%d"))
        nowConfirm.append(ri[1])
        confirm.append(ri[2])
        heal.append(ri[3])
        dead.append(ri[4])

    return jsonify({"day": day, "nowConfirm": nowConfirm, "confirm": confirm,
                    "heal": heal, "dead": dead})


@app.route("/l2")
def getL2():
    ret = db.session.query(History.time, History.confirm_add, History.heal_add, History.dead_add).all()
    ret = ret[7:]

    day, confirm_add, heal_add, dead_add = [], [], [], []

    for ri in ret:
        day.append(ri[0].strftime("%m-%d"))
        confirm_add.append(ri[1])
        heal_add.append(ri[2])
        dead_add.append(ri[3])

    return jsonify({"day": day, "confirm_add": confirm_add,
                    "heal_add": heal_add, "dead_add": dead_add})


@app.route("/r1")
def getR1():
    ret = db.session.query(Province.province, Province.confirm).order_by(Province.confirm.desc()).limit(10).all()

    province, confirm = [], []
    for ri in ret:
        province.append(ri[0])
        confirm.append(ri[1])

    return jsonify({"province": province, "confirm": confirm})


@app.route("/r2/<province>")
def getR2(province):
    ret = db.session.query(Details.city, Details.confirm).filter(Details.province == province)
    ret = list(ret)

    res = []
    for ri in ret:
        res.append({"name": ri[0], "value": int(ri[1])})

    print(res)
    return jsonify({"res": res})


@app.route("/", methods=["post","get"])
def index():
    calen = cal.Calendar()
    return render_template("index.html", calen=calen)


@app.route("/search", methods=["post", "get"])
def search():
    month = request.args.get("month")
    day = request.args.get("day")

    date = "2020-" + month + "-" + day
    ret = db.session.query(Province.province, Province.confirm).filter(Province.update_time == date).all()

    res = []
    for ri in ret:
        res.append({"name": ri[0], "value": int(ri[1])})

    return jsonify({"res": res})


if __name__ == '__main__':
    app.run(debug=True)
