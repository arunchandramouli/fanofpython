

var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';

page.open('https://www.walmart.com/browse/auto-tires/car-truck-tires/91083_1077064_1063465', function(status) {

  if (status !== 'success') {
    console.log('Unable to access network');

  } 
  	else {
    	var ua = page.evaluate(function() {
              var matches = [];
      				var prd_details = document.getElementsByClassName('tile-heading');
              for (var i=0;i<prd_details.length;i++){

                  matches.push(prd_details[i].textContent);
              }

              return matches
    });

      console.log("Processing ! ");
      console.log(ua);    
  }
  
  phantom.exit();
});

