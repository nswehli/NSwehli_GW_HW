// Use D3 to select the table body
var body = d3.select("tbody")

// Use D3 to select the table
var table = d3.select(".grades")
// Use D3 to set the table class to `table table-striped`

table.attr("class", "table table-striped");

// Loop through an array of grades and build the entire table body from scratch
var grades = [["Malcolm", 80], ["Zoe", 85], ["Kaylee", 99], ["Simon", 99], ["Wash", 79]];

grades.forEach(grade => {
    var row = body.append("tr")
    row.append("td").text(grade[0]);
    row.append("td").text(grade[1]);
});
