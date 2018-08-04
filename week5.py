import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_92868.xml'
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
comment = tree.findall('comments/comment')
sum = 0
for item in comment:
    number = item.find('count').text
    sum+=int(number)
print(sum)


    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
    #
    # print('lat', lat, 'lng', lng)
    # print(location)
