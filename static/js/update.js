function gettime() {
    $.ajax({
        url: "/time",
        timeout: 10000, //超时时间设置为10秒；
        success: function (data) {
            $("#time").html(data)
        }
    });
}

function getDataC1() {
    $.ajax({
        url: "/c1",
        success: function (data) {
            $(".num").eq(0).text(data.confirm);
            $(".num").eq(1).text(data.heal);
            $(".num").eq(2).text(data.dead);
            $(".stxt").eq(0).text("较上日" + data.confirm_add);
            $(".stxt").eq(1).text("较上日" + data.heal_add);
            $(".stxt").eq(2).text("较上日" + data.dead_add);
        }
    });
}

function getDataC2() {
    $.ajax({
        url: "/c2",
        success: function (data) {
            $(".num").eq(3).text(data.nowConfirm);
            $(".num").eq(4).text(data.noInfect);
            $(".num").eq(5).text(data.importedCase);
            $(".stxt").eq(3).text("较上日" + data.nowConfirm_add);
            $(".stxt").eq(4).text("较上日" + data.noInfect_add);
            $(".stxt").eq(5).text("较上日" + data.importedCase_add);
        }
    });
}

function getMap() {
    $.ajax({
        url: "/c3",
        success: function (data) {
            mapOption.series[0].data = data.res;
            center.setOption(mapOption);
        }
    });
}


$("form").submit(function () {
   $.ajax({
       url: "/search",
       data:$("#date_search").serialize(),
       success: function (da) {
            mapOption.series[0].data = da.res;
            center.setOption(mapOption);
       }
   });

   return false;
});


function getDataL1() {
    $.ajax({
        url: "/l1",
        success:function (data) {
            left1_option.xAxis[0].data = data.day;
            left1_option.series[0].data = data.nowConfirm;
            left1_option.series[1].data = data.confirm;
            left1_option.series[2].data = data.heal;
            left1_option.series[3].data = data.dead;
            left1.setOption(left1_option);
        }
    });
}

function getDataL2() {
    $.ajax({
        url: "/l2",
        success:function (data) {
            left2_option.xAxis[0].data = data.day;
            left2_option.series[0].data = data.confirm_add;
            left2_option.series[1].data = data.heal_add;
            left2_option.series[2].data = data.dead_add;
            left2.setOption(left2_option);
        }
    })
}

function getDataR1() {
    $.ajax({
        url: "/r1",
        success:function (data) {
            right1_option.xAxis[0].data = data.province;
            right1_option.series[0].data = data.confirm;
            right1.setOption(right1_option);
        }
    });
}

getDataC1();
getDataC2();
getMap();
getDataL1();
getDataL2();
getDataR1();
setInterval(gettime, 1000);
// setInterval(getDataC1, 1000);
// setInterval(getDataC2, 1000);