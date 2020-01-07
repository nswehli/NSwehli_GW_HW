// Create an array of each country's numbers
var us = Object.values(data.us);
var uk = Object.values(data.uk);
var canada = Object.values(data.canada);

var us_labels = Object.keys(data.us);
var uk_labels = Object.keys(data.uk);
var canada_labels = Object.keys(data.canada);

console.log(us_labels)



// @ADD YOUR CODE HERE

var data = [{
    values: us,
    labels: us_labels,
    type: 'pie'
}];

var layout = {
    height: 400,
    width: 500
};

Plotly.newPlot('pie', data, layout);

d3.selectAll("#selDataset").on("change", updatePlotly);

function updatePlotly() {
    // Use D3 to select the dropdown menu
    var selection = d3.select("#selDataset").property("value");
    // Assign the value of the dropdown menu option to a variable
    // var dataset = dropdownMenu.property("value");
    values: [];
    labels: [];
    switch (selection) {
        case "US":
            values = us;
            labels = us_labels;
            break;
        case "Canada":
            values = canada;
            labels = canada_labels;
            break;
        case "UK":
            values = uk;
            labels = uk_labels;
            break
    }

    Plotly.restyle("pie", "values", [values]);
    Plotly.restyle("pie", "labels", [labels]);
}
