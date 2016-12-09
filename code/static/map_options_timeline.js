
function MapOption(){
    this.option = {
            baseOption:{
                timeline:{
                    axisType: 'category',
                    data: []
                },
                title: {
                    text: '人口分布',
                    subtext: '历年人口变化',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: ['总人口','流出人口','流入人口','净流入']
                },
                visualMap: {
                    min: 0,
                    max: 100000000,
                    left: 'left',
                    top: 'bottom',
                    text: ['高', '低'],
                    calculable: true
                },
                toolbox: {
                    show: true,
                    orient: 'vertical',
                    left: 'right',
                    top: 'center',
                    feature: {
                        mark: {show: true},
                        dataView: {show: true, readOnly: false},
                        restore: {show: true},
                        saveAsImage: {show: true}
                    }
                },
                series:[]
            },
            options:[]
        };

    this.provinces = [
        '北京','天津','上海','重庆','河北','河南','云南','辽宁','黑龙江','湖南','安徽','山东','新疆','江苏','浙江','江西','湖北','广西','甘肃','山西','内蒙古','陕西','吉林','福建','贵州','广东','青海','西藏','四川','宁夏','海南','台湾','香港','澳门'
    ]

    this.getProvinceName = function(longName){
        for(var i = 0;i<this.provinces.length;i++){
            if(longName.indexOf(this.provinces[i]) >= 0){
                return this.provinces[i];
            }
        }
    }
    this.appendTimeline = function(year){
        this.option.baseOption.timeline.data.push(year);
    }

    this.baseSeriesOption = function(){
        return {
                name: '人口分布',
                type: 'map',
                mapType: 'china',
                roam: false,
                label: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: true
                    }
                },
                data:[]
            };
    };

    this.setMaxValue = function(value){
        this.option.visualMap.max = value;
    }

    this.setSeries = function(data){
        this.option.baseOption.series.push(data);
    }

    this.setSeriesData = function(data){
        this.option.options.push(data);
    }
}