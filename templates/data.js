let globalData;
function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#movieTitle");

  // Use the list of sample names to populate the select options
  d3.csv("../Data/movies_metadata.csv").then((data) => {

    for (var i = 0; i < 700; i++) {
      var title = data[i].original_title;
      selector
        .append("option")
        .text(title)
        .property("value", title);
    }
    globalData = data; 
    var firstTitle = data[0].original_title;
    optionChanged(firstTitle)
    // Use the first sample from the list to build the initial plots
    //var firstSample = sampleNames[0];
  });
}

// Initialize the dashboard
init();
function optionChanged(titleParam) {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#movieGenre");
  d3.select("#movieGenre").selectAll("*").remove();
  var genres = eval(findGenres(titleParam));

  for (var j = 0; j<genres.length; j++) {
    selector
      .append("input").text(genres[j]["name"])
      .property("type", "text")
      .property("name", "genre"+eval(j+1))
      .property("value", genres[j]["name"])
      .attr("readonly","true");
  }
  console.log(titleParam);
}


function findGenres(title){
    // Use the list of sample names to populate the select options
       var titleObject = globalData.filter(x=>x.original_title == title);
       return titleObject[0].genres;
}
