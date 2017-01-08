
var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request("https://www.walmart.com/browse/auto-tires/car-truck-tires/91083_1077064_1063465?page=2", function(error, response, body) {
  
  if(error) {
    console.log("Error: " + error);
  }
  
  console.log("Status code: " + response.statusCode);

  var $ = cheerio.load(body);

  $('.tile-grid-unit-wrapper').each(function( index ) {

      var title = $(this).find('.tile-heading>div').text().trim();
      var price = $(this).find('.price.price-display').text().trim();     

      console.log("Title: " + title);
      console.log("Price: " + price);
      
    fs.appendFileSync('wall.txt', title + '\n' + price + '\n' + user + '\n');
  });

});

