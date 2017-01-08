
var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request("https://careers.google.com/jobs#t=sq&q=j&li=20&l=false&j=Hyderabad", function(error, response, body) {
  
  if(error) {
    console.log("Error: " + error);
  }
  
  console.log("Status code: " + response.statusCode);

  var $ = cheerio.load(body);

  console.log(body);


  $('.sr-content').each(function( index ) {



      var title = $(this).find('.sr-title.text>span').text().trim();
      
      console.log("Title: " + title);

  });

});

