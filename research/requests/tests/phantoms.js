

var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';

page.open('https://careers.google.com/jobs#t=sq&q=j&li=20&l=false&j=Hyderabad', function(status) {

  if (status !== 'success') {
    console.log('Unable to access network');

  } 

  	else {
    	var ua = page.evaluate(function() {
        
      				var sx = document.getElementsByClassName('sr-title text');
              return sx.length;
    });

    console.log(ua);
  }
  
  phantom.exit();
});

