var right1 = echarts.init(document.getElementById("r1"),"dark");

var right1_option = {
	title: {
		text: '新增确诊分布',
		textStyle: {
			color: 'white'
		},
		left: 'left'
	},
	color: ['#3398DB'],
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'shadow'
		}
	},

	xAxis: [{
		type: 'category',
        axisLabel :{
                interval:0
            },
		data: []
	}],
	yAxis: {
		type: 'value',
		//坐标轴刻度设置
		},
	series: [{
		type: 'bar',
		data: [],
		barMaxWidth: "50%"
	}]
};

right1.setOption(right1_option);
