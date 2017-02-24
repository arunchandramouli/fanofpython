
import requests



headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
 "x-csrf-token":"1487909373-01-teiUDW9KvRP4ZyH7uTSV-X80rQHDn-RjabK2oGXUrIo",
 'Accept': 'application/json, text/javascript, */*; q=0.01',
 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 'X-Requested-With': 'XMLHttpRequest'
}


data = {"targetLocation":{"latitude":41.8781136,"longitude":-87.6297982,"address":{"title":"Chicago","address1":"Chicago","city":"Chicago"}}}


url="https://www.ubereats.com/rtapi/eats/v1/bootstrap-eater"


print requests.post(url="https://www.ubereats.com/rtapi/eats/v1/bootstrap-eater",data=data,headers=headers)


