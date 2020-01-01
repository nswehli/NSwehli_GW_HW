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

// List of values
var button = d3.select("#filter-btn");

var Date = data.map(element => element.datetime);
var City = data.map(element => element.city.toUpperCase());
var State = data.map(element => element.state.toUpperCase());
var Country = data.map(element => element.country.toUpperCase());
var Shape = data.map(element => element.shape.toUpperCase());


// Lists of Unique Values
listofCities = City.filter(function (x, i, a) {
    return a.indexOf(x) == i;
}).sort();


listofDate = Date.filter(function (x, i, a) {
    return a.indexOf(x) == i;
});

listofStates = State.filter(function (x, i, a) {
    return a.indexOf(x) == i;
}).sort();

listofCountries = Country.filter(function (x, i, a) {
    return a.indexOf(x) == i;
});

listofShapes = Shape.filter(function (x, i, a) {
    return a.indexOf(x) == i;
}).sort();



// updating list of choices from data
var datasearch = d3.select("#dates")
var citysearch = d3.select("#cities")
var statesearch = d3.select("#states")
var countrysearch = d3.select("#countries")
var shapesearch = d3.select("#shapes")


listofDate.forEach(date => {
    var row = datasearch.append("option")
    row.append("option").text(date);
});

listofCities.forEach(city => {
    var row = citysearch.append("option")
    row.append("option").text(city);
});

listofStates.forEach(state => {
    var row = statesearch.append("option")
    row.append("option").text(state);
});

listofCountries.forEach(country => {
    var row = countrysearch.append("option")
    row.append("option").text(country);
});

listofShapes.forEach(shape => {
    var row = shapesearch.append("option")
    row.append("option").text(shape);
});

var datebutton = d3.select("#dateFilterButton");

datebutton.on("click", function () {
    console.log("Date search button was clicked");
    var inputinfo = d3.select("#dates").property("value")
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
})

var citybutton = d3.select("#cityFilterButton");

citybutton.on("click", function () {
    console.log("City search button was clicked");
    var inputinfo = d3.select("#cities").property("value").toLowerCase()
    function search(city) {
        return city.city == inputinfo;
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
})


var statebutton = d3.select("#stateFilterButton");

statebutton.on("click", function () {
    console.log("State search button was clicked");
    var inputinfo = d3.select("#states").property("value").toLowerCase()
    function search(state) {
        return state.state == inputinfo;
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
})

var countrybutton = d3.select("#countriesFilterButton");

countrybutton.on("click", function () {
    console.log("Countries search button was clicked");
    var inputinfo = d3.select("#countries").property("value").toLowerCase()
    function search(country) {
        return country.country == inputinfo;
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
})

var shapebutton = d3.select("#shapeFilterButton");

shapebutton.on("click", function () {
    console.log("Shape search button was clicked");
    var inputinfo = d3.select("#shapes").property("value").toLowerCase()
    function search(shape) {
        return shape.shape == inputinfo;
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
})

var showAllbutton = d3.select("#showAllButton");

showAllbutton.on("click", function () {
    console.log("Show-all search button was clicked");

    d3.select(".table").selectAll("td").remove()
    data.forEach(item => {
        var row = body.append("tr")
        row.append("td").text(item.datetime);
        row.append("td").text(item.city);
        row.append("td").text(item.state);
        row.append("td").text(item.country);
        row.append("td").text(item.shape);
        row.append("td").text(item.durationMinutes);
        row.append("td").text(item.comments);
    })
})


