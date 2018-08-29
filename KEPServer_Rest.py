import requests
import json

rest_browse = requests.get('http://127.0.0.1:39320/iotgateway/browse')
data_browse = json.loads(rest_browse.text)
for x in range(len(data_browse['browseResults'])):
    rest = requests.get('http://127.0.0.1:39320/iotgateway/read?ids='+data_browse['browseResults'][x]['id'])
    data = json.loads(rest.text)
    print(data)
    print("Tag Name=", data['readResults'][0]['id'], "   ", "Value", data['readResults'][0]['v'])