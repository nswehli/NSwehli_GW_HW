// from results.js

var body = d3.select("tbody")

// Use D3 to select the table
var table = d3.select(".table")

data.forEach(item => {
    var row = body.append("tr")
    row.append("td").text(item.datetime);
    row.append("td").text(item.city);
    row.append("td").text(item.state);
    row.append("td").text(item.country);
    row.append("td").text(item.shape);
    row.append("td").text(item.durationMinutes);
    row.append("td").text(item.comments);
});

var button = d3.select("#filter-btn");

button.on("click", function () {
    console.log("Search button was clicked");
    var inputinfo = d3.select("#datetime").property("value")

    if (inputinfo == "") {
        data.forEach(item => {
            var row = body.append("tr")
            row.append("td").text(item.datetime);
            row.append("td").text(item.city);
            row.append("td").text(item.state);
            row.append("td").text(item.country);
            row.append("td").text(item.shape);
            row.append("td").text(item.durationMinutes);
            row.append("td").text(item.comments);
        });

    } else {
        function search(date) {
            return date.datetime == inputinfo;
        }
        console.log("Entered value is: " + inputinfo);
        var results = data.filter(search);
        console.log(results);
        d3.select(".table").selectAll("td").remove()
        results.forEach(item => {
            var row = body.append("tr")
            row.append("td").text(item.datetime);
            row.append("td").text(item.city);
            row.append("td").text(item.state);
            row.append("td").text(item.country);
            row.append("td").text(item.shape);
            row.append("td").text(item.durationMinutes);
            row.append("td").text(item.comments);
        });
    }

});

