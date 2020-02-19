//
var myMap = L.map("map", {
    center: [32.99261, -9.8598969],
    zoom: 3,
    scrollWheelZoom: false
});

const API_KEY = "pk.eyJ1IjoibnN3ZWhsaSIsImEiOiJjazVnMnc2ZHowM244M2pxbTFlYWhzMXVwIn0.0CxW_QdppTZUjpTaUh8-dQ"


// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
}).addTo(myMap);

//getting data for Past 30 Days earthquakes

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
d3.json(url).then(function (response) {
    console.log(response)
    var dateR = new Date(response.metadata.generated)
    d3.select("#Headline").text(response.metadata.title)
    d3.select("#date").text(response.metadata.title)

    var data = response.features
    for (var i = 0; i < data.length; i++) {

        var date = new Date(data[i].properties.time)

        var color = "";
        if (data[i].properties.mag >= 4.5) {
            color = "#fc1b2d";
        }
        else if (data[i].properties.mag > 2.5) {
            color = "#ff5a1a";
        }

        else {
            color = "#ffa600";
        }
        L.circle([data[i].geometry.coordinates[1], data[i].geometry.coordinates[0]], {
            fillOpacity: 0.75,
            color: "grey",
            fillColor: color,


            // Setting our circle's radius equal to the output of our markerSize function
            // This will make our marker's size proportionate to its population
            radius: data[i].properties.mag * 50000
        }).bindPopup("<h1>" + data[i].properties.title + "</h1> <hr> <h3>Event: " + data[i].properties.type + " on " + date + "</h3>").addTo(myMap);
    }


    // var legend = L.control({ position: "topright" });
    // legend.onAdd = function () {
    //     var div = L.DomUtil.create("div", "info legend");
    //     // var limits = geojson.options.limits;
    //     // var colors = geojson.options.colors;
    //     var labels = ["Test", "Test01"];

    //     // Add min & max
    //     var legendInfo = `<h1> ${response.metadata.title} </h1>`
    //     // "<div class=\"labels\">" +
    //     // "<div class=\"min\">" + limits[0] + "</div>" +
    //     // "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
    //     // "</div>";

    //     div.innerHTML = legendInfo;

    //     labels.forEach(function (limit, index) {
    //         labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    //     });

    //     div.innerHTML += "<ul>" + "Test" + "</ul>";
    //     return div;
    // };

    // // Adding legend to the map
    // legend.addTo(myMap);

    // }
    console.log("Done")

})



// // Loop through the cities array and create one marker for each city object
// for (var i = 0; i < cities.length; i++) {
//     L.circle([data[i].geometry.coordinates[1], data[i].geometry.coordinates[0]], {
//       fillOpacity: 0.75,
//       color: "white",
//       fillColor: "purple",
//       // Setting our circle's radius equal to the output of our markerSize function
//       // This will make our marker's size proportionate to its population
//       radius: markerSize(data[i].properties.mag)
//     }).bindPopup("<h1>" + data[i].properties.title + "</h1> <hr> <h3>Link: " + data[i].properties.url + "</h3>").addTo(myMap);
//   }

