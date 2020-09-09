var left2 = echarts.init(document.getElementById("l2"), "dark");

var left2_option = {
    title: {
        text: '全国新增趋势',
        textStyle: {},
        left: 'left'
    },

    legend: {
        data: ['新增确诊', '新增治愈', '新增死亡'],
        left: 'right'
    },

    //  图表距边框的距离,可选值：'百分比'¦ {number}（单位px）
    grid: {
        top: 50, // 等价于 y: '16%'
        left: '4%',
        right: '6%',
        bottom: '4%',
        containLabel: true
    },

    // 提示框
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: '#7171C6'
            }
        }
    },

    xAxis: [{
        type: 'category',
        data: []
    }],

    yAxis: [{
        type: 'value',
        axisLine: {
            show: true
        },
        axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
            formatter: function (value) {
                if (value >= 1000) {
                    value = value / 1000 + 'k';
                }
                return value;
            }
        },
        splitLine: {
            show: true,
            lineStyle: {
                color: '#172738',
                width: 1,
                type: 'solid'
            }
        }
    }],

    series: [{
        name: '新增确诊',
        data: [],
        type: 'line',
        // 设置小圆点消失
        // 注意：设置symbol: 'none'以后，拐点不存在了，设置拐点上显示数值无效
        // symbol: 'none',
        // 设置折线弧度，取值：0-1之间
        smooth: true
    },
        {
            name: '新增治愈',
            data: [],
            type: 'line',
            // 设置折线上圆点大小
            smooth: true
        },
        {
            name: '新增死亡',
            data: [],
            type: 'line',
            // 设置折线上圆点大小
            smooth: true
        }
    ]
};

left2.setOption(left2_option);
