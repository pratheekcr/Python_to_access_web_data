import urllib.request, urllib.parse, urllib.error
import json

link = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter the link address')
html = link + urllib.parse.urlencode({'address':address})
fhand = urllib.request.urlopen(html)
data = fhand.read().decode()
js = json.loads(data)
print(json.dumps(js, indent = 4))
print('len',len(js))
print('place_id',js['results'][0]['place_id'])
# South Federal University