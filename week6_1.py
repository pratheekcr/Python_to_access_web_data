import urllib.parse, urllib.request, urllib.error
import json

html = 'http://py4e-data.dr-chuck.net/comments_92869.json'
fhand = urllib.request.urlopen(html)
data = fhand.read().decode()
print(data)
js = json.loads(data)
# print(json.dumps(js, indent=4))
sum=0
for item in js['comments']:
    count = item['count']
    sum+=count
print(sum)


