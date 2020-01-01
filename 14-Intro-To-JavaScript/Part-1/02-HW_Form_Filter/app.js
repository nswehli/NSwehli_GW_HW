// Assign the data from `data.js` to a descriptive variable
var people = data;

// Select the button
var button = d3.select("#button");

// Complete the click handler for the form

// button.on("click", function () {
//   console.log("Patient Data button was clicked");
//   var inputinfo = d3.select("#patient-form-input").property("value")
//   console.log("Entered value is :" + inputinfo);

// });

// Select the input element and get the raw HTML node
var form = d3.select(".form-group").html()
console.log(form)

// Get the value property of the input element

var inputinfo = d3.select("#patient-form-input").property("value")

console.log("Entered value is :" + inputinfo)

// Use the form input to filter the data by blood type
function bloodType(type) {
  return type.bloodType == inputinfo;
}

// filter() uses the custom function as its argument
// var bloodTypes = data.filter(bloodType);
// console.log("test")
// console.log(bloodTypes)
// console.log("Blood Types" + bloodTypes);

button.on("click", function () {
  console.log("Patient Data button was clicked");
  var inputinfo = d3.select("#patient-form-input").property("value")
  function bloodType(type) {
    return type.bloodType == inputinfo;
  }
  console.log("Entered value is :" + inputinfo);
  var bloodTypes = data.filter(bloodType);
  console.log(bloodTypes);
  var ageData = bloodTypes.map(element => element.age);
  console.log(ageData);
  var median = math.median(ageData);
  var mean = math.round(math.mean(ageData), 1);
  var mode = math.mode(ageData);
  var variance = math.round(math.variance(ageData), 1);
  var std = math.round(math.std(ageData), 1);
  console.log("Median is " + median);
  d3.select("ul").text("")
  d3.select("ul").append("li").text("Median age is " + median);
  d3.select("ul").append("li").text("Mean age is " + mean);
  d3.select("ul").append("li").text("Mode age is " + mode);
  d3.select("ul").append("li").text("Variance of age is " + variance);
  d3.select("ul").append("li").text("Standard Deviation of age is " + std);
  ;

});
  // BONUS: Calculate summary statistics for the age field of the filtered data

  // First, create an array with just the age values

  // Next, use math.js to calculate the mean, median, mode, var, and std of the ages

  // Finally, add the summary stats to the `ul` tag

