var chartDataString = decodeHTML(chartData);
var chartJsonArray = JSON.parse(chartDataString);

var arrayLength =chartJsonArray.length;
var numericData = [];
var labelData = [];

for(var i=0; i<arrayLength; i++){
    numericData[i] = chartJsonArray[i].value;
    labelData[i] = chartJsonArray[i].label;
}


// For a pie chart
new Chart(document.getElementById("myPieChart"),{
    type: 'pie',
    // The data for our set
    data: {
            labels: labelData,
            datasets: [{
                label: 'Projects by Status',
                data: numericData,
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
                borderWidth: 1
            }]
        },
        // Configuration options go here
        options: {
            plugins: {
                title: {
                    display : true,
                    text: 'Project Statuses'
                }
            }
        }
        });

// What to expect (3 arrays):
// [{"value" : 1, "label" : NOTSTARTED},{"value" : 2, "label" : "INPROGRESS"},{"value" : 1, "label" : "COMPLETED}]
 function decodeHTML(html){
    var txt  = document.createElement("textarea");
    txt.innerHTML =html;
    return txt.value;
}
