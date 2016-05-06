var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */

 function newDeviceID() {
     new_device_id = document.getElementById("device-id-input").value;
     requestDeviceData(new_device_id);
 }

function requestData() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

function requestDeviceData(id) {
    var s = ["/device", id]
    var device_url = s.join("/");
    console.log(device_url)
    $.ajax({
        url: device_url,
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestDeviceData(id), 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart1 = new Highcharts.Chart({
        chart: {
            renderTo: 'avg-speed-on-earth',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Average Wind Speed on Earth'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },
        series: [{
            name: 'Wind Speed (knots)',
            data: []
        }]
    });

    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'avg-speed-device',
            defaultSeriesType: 'spline',
            events: {
                load: requestDeviceData
            }
        },
        title: {
            text: 'Avg Device Speed'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },
        series: [{
            name: 'Wind Speed (knots)',
            data: []
        }]
    });

});
