function master(){

              var page = require('webpage').create();
              console.log('The default user agent is ' + page.settings.userAgent);
              page.settings.userAgent = 'SpecialAgent';

              page.open(arguments[0], function(status) {

                    if (status !== 'success') {
                      console.log('Unable to access network');

                    } 
                    
                    else {
                                console.log("scrape_page__call__")
                                //return scrape_page();

                                var matches = [];
                                var prd_details = document.getElementsByClassName('tile-heading');
                                console.log(prd_details[i].length);

                                for (var i=0;i<prd_details.length;i++){

                                    matches.push(prd_details[i].textContent);
                                    console.log(prd_details[i].textContent);
                                }

                                
                                
                          }

              phantom.exit();
      });
}

master('https://www.walmart.com/browse/auto-tires/car-truck-tires/91083_1077064_1063465')


function scrape_page(){

            var scrap =  page.evaluate(function() {

                              console.log(true);

                              var matches = [];
                              var prd_details = document.getElementsByClassName('tile-heading');

                              for (var i=0;i<prd_details.length;i++){

                                  matches.push(prd_details[i].textContent);
                              }

                              return matches

                          });

            console.log(scrap);

}