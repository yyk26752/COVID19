
// // 目录下所有地名
let arr = ['anhui.js', 'aomen.js', 'beijing.js', 'chongqing.js',
    'fujian.js', 'gansu.js', 'guangdong.js', 'guangxi.js', 'guizhou.js',
    'hainan.js', 'hebei.js', 'heilongjiang.js', 'henan.js', 'hubei.js',
    'hunan.js', 'index.js', 'jiangsu.js', 'jiangxi.js', 'jilin.js',
    'liaoning.js', 'neimenggu.js', 'ningxia.js', 'qinghai.js',
    'shandong.js', 'shanghai.js', 'shanxi.js', 'shanxi1.js',
    'sichuan.js', 'taiwan.js', 'tianjin.js', 'xianggang.js',
    'xinjiang.js', 'xizang.js', 'yunnan.js', 'zhejiang.js'];
// 路径公共的字符串
let pre = '../static/js/province/';

// 遍历数组
arr.forEach(item=>{
  document.write("<script src='"+pre + item + "'></script>");
});


// document.write("<script src='../static/js/province/anhui.js'></script>");
// document.write("<script src='../static/js/province/aomen.js'></script>");


