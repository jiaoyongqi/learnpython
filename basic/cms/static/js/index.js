//数据准备,
var points = [];//原始点信息数组
var bPoints = [];//百度化坐标数组。用于更新显示范围。
var datashowarr = [];
var statusinfoarr = [];
var gpstest_i = 0;
var lngtest = [116.0638454, 116.0638442, 116.0638425, 116.0638412, 116.0638336, 116.0638169, 116.0637966, 116.0637394,116.0635821,116.063559,116.0635244];
var lattest = [40.1914438, 40.1914505, 40.1914594, 40.1914665, 40.1915090, 40.1915867, 40.1916361, 40.1916938, 40.1917132,40.1917106,40.1917062];

function  dataClassify(data){
    // console.log(data)
    datashowarr.splice(0,datashowarr.length);//清空数组
    statusinfoarr.splice(0,statusinfoarr.length);

    //基本信息
    var targeArr = {}
    var targeBackArr = {}
    targeArr = {"name":"车辆信息","value":"TD90"}
    datashowarr.push(targeArr)
    targeArr = {"name":"目前车速","value":data.fVTagSpd}
    datashowarr.push(targeArr)
    targeArr = {"name":"任务编号","value":data.tTaskID}
    datashowarr.push(targeArr)
    targeArr = {"name":"前置雷达前方","value":data.Front_Obstacle0}
    datashowarr.push(targeArr)
    targeArr = {"name":"前置雷达左侧","value":data.Front_Obstacle1}
    datashowarr.push(targeArr)
    targeArr = {"name":"前置雷达右侧","value":data.Front_Obstacle2}
    datashowarr.push(targeArr)
    targeArr = {"name":"前置雷达左车道","value":data.Front_Obstacle3}
    datashowarr.push(targeArr)
    targeArr = {"name":"前置雷达右车道","value":data.Front_Obstacle4}
    datashowarr.push(targeArr)
    targeArr = {"name":"后置雷达前方","value":data.Back_Obstacle0}
    datashowarr.push(targeArr)
    targeArr = {"name":"后置雷达左侧","value":data.Back_Obstacle1}
    datashowarr.push(targeArr)
    targeArr = {"name":"后置雷达右侧","value":data.Back_Obstacle2}
    datashowarr.push(targeArr)
    targeArr = {"name":"后置雷达左车道","valiue":data.Back_Obstacle3}
    datashowarr.push(targeArr)
    targeArr = {"name":"后置雷达右车道","value":data.Back_Obstacle4}
    datashowarr.push(targeArr)
    // console.log(datashowarr)

    //状态信息
    targeBackArr = {"name":"经度","value":data.gLng}
    statusinfoarr.push(targeBackArr)
    targeBackArr = {"name":"纬度","value":data.gLat}
    statusinfoarr.push(targeBackArr)
    targeBackArr = {"name":"定位状态","value":data.gRTK}
    statusinfoarr.push(targeBackArr)
    //targeBackArr = {"name":"急停状态","value":data.cEmergentOffLine}
    //statusinfoarr.push(targeBackArr)
    targeBackArr = {"name":"档位状态","value":data.ve_shift}
    statusinfoarr.push(targeBackArr)
    targeBackArr = {"name":"翻斗状态","value":data.ve_bucket}
    statusinfoarr.push(targeBackArr)
    //targeBackArr = {"name":"采集板状态","value":data.cCollectOffLine}
    //statusinfoarr.push(targeBackArr)
    //targeBackArr = {"name":"毫米波雷达","value":data.cRadarOffLine}
    //statusinfoarr.push(targeBackArr)
    //targeBackArr = {"name":"前置雷达状态","value":data.qLidarFrontStaus}
    //statusinfoarr.push(targeBackArr)
    //targeBackArr = {"name":"后置雷达状态","value":data.qLidarBackOffLine}
    //statusinfoarr.push(targeBackArr)
    //targeBackArr = {"name":"执行机构状态","value":data.robotOffLine}
    //statusinfoarr.push(targeBackArr)
    targeBackArr = {"name":"是否进入挖掘地","value":data.receive_responseCmd}
    statusinfoarr.push(targeBackArr)
    targeBackArr = {"name":"是否驶出挖掘地","value":data.receive_driveCmd}
    statusinfoarr.push(targeBackArr)
    // console.log(statusinfoarr)

}


function dealData(){
    // console.log(res)
    var html;
    var htmlinfo;

    //数据显示
    $('#datashow tbody').html('')
    for(var i = 0;i < datashowarr.length;i++)
    {
        // console.log(datashowarr[i].name);
        // console.log(datashowarr[i].value);

        var tr = '<tr>' +
        '<td>' + datashowarr[i].name + '</td>' +
        '<td>' + datashowarr[i].value + '</td>' +
        '</tr>'
        html += tr;
        // console.log(html)
    }
    $('#datashow tbody').append(html);

    //状态信息
    $('#statusinfo tbody').html('')
    for(var i = 0;i < statusinfoarr.length;i++)
    {
        // console.log(statusinfoarr[i].name);
        // console.log(statusinfoarr[i].value);

        var tr = '<tr>' +
        '<td>' + statusinfoarr[i].name + '</td>' +
        '<td>' + statusinfoarr[i].value + '</td>' +
        '</tr>'
        htmlinfo += tr;
        // console.log(htmlinfo)
    }
    $('#statusinfo tbody').append(htmlinfo);

    // $('.table tbody tr td:nth-child(even)')
}

//获取后端数据
setInterval(function query() {
            $.ajax({
                url: "test_post/nn",
                type: "POST",
                // data: senddata,
                dataType: "json",
                success: function (data) {
                    console.log(data)
                    dataClassify(data)
                    dealData()
                }
            })
        }, 1000);

//地图操作开始
var map = new BMap.Map("container");

map.centerAndZoom(new BMap.Point(103.388611, 35.563611), 5); //初始显示中国。

// map.enableScrollWheelZoom();//滚轮放大缩小
map.disableDragging();//禁止地图拖拽

setTimeout(dynamicLine, 1000);//动态生成新的点。
//添加线
function addLine(points) {

    var linePoints = [], pointsLen = points.length, i, polyline;
    if (pointsLen == 0) {
        return;
    }
    // 创建标注对象并添加到地图   
    for (i = 0; i < pointsLen; i++) {
        linePoints.push(new BMap.Point(points[i].lng, points[i].lat));
    }

    polyline = new BMap.Polyline(linePoints, { strokeColor: "red", strokeWeight: 2, strokeOpacity: 0.5 });   //创建折线
    map.addOverlay(polyline);   //增加折线
}

//随机生成新的点，加入到轨迹中。
function dynamicLine() {
    var lng = lngtest[gpstest_i];
    var lat = lattest[gpstest_i];
    if (gpstest_i == 10)
        gpstest_i=0;

    gpstest_i++;

    var id = getRandom(1000);
    var point = { "lng": lng, "lat": lat, "status": 1, "id": id }
    var makerPoints = [];
    var newLinePoints = [];
    var len;

    makerPoints.push(point);
    addMarker(makerPoints);//增加对应该的轨迹点
    points.push(point);
    bPoints.push(new BMap.Point(lng, lat));
    len = points.length;
    newLinePoints = points.slice(len - 2, len);//最后两个点用来画线。

    addLine(newLinePoints);//增加轨迹线
    setZoom(bPoints);
    setTimeout(dynamicLine, 1000);
}

// 获取随机数
function getRandom(n) {
    return Math.floor(Math.random() * n + 1)
}

//根据点信息实时更新地图显示范围，让轨迹完整显示。设置新的中心点和显示级别
function setZoom(bPoints) {
    var view = map.getViewport(eval(bPoints));
    var mapZoom = view.zoom;
    var centerPoint = view.center;
    map.centerAndZoom(centerPoint, mapZoom);
}

function addMarker(points) {  // 创建图标对象   
    var point, marker;
    // 创建标注对象并添加到地图   
    for (var i = 0, pointsLen = points.length; i < pointsLen; i++) {
        point = new BMap.Point(points[i].lng, points[i].lat);
        marker = new BMap.Marker(point);
        map.addOverlay(marker);
        //给标注点添加点击事件。使用立即执行函数和闭包
        (function () {
            var thePoint = points[i];
            marker.addEventListener("click", function () {
                showInfo(this, thePoint);
            });
        })();
    }
}
