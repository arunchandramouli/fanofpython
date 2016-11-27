import requests

URL = "https://www.stayzilla.com/search?"

#http://stackoverflow.com/questions/12756443/fill-and-submit-html-form

payload = {
	
	'input-grp__input input__query-text js-search-box':'Kodaikanal',
	'date-grp__icon input-grp__icon':'Wed, 30th Nov',
	'date-grp__date':'Sat,3rd Dec',
	'options-group__heading':'Man',
	'search-form__submit':'Search'
}

load = {
	
	'area':'Kodaikanal',
	'checkInDate':'29-11-2016',
	'checkOutDate':'30-11-2016',
	'city':'Kodaikanal',
	'name':'Kodaikanal',
	'queryText':'Kodaikanal'
}

session = requests.session()
r = requests.post(URL, params=load,verify=False)
print r.url

'''
https://www.stayzilla.com/search?area=Kodaikanal&checkInDate=30-110-2016&checkOutDate=03-12-2016&city=Kodaikanal&name=Kodaikanal&queryText=Kodaikanal
'''
