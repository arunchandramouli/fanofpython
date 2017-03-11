var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';


page.open('https://careers.google.com/', function (status) {

    if (status !== 'success') {
        console.log('Unable to load the address!');
    } 

    else {

          window.setTimeout(function () {

                  var select_ip_text_box = document.getElementsByTagName('*');

                  console.log(select_ip_text_box.length);
                  
                  phantom.exit();

          }, 200);
    }
});
