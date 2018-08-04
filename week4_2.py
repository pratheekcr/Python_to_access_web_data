import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


def access_links(req_tag, count, position):
    while count>0:
        count = count-1
        href = req_tag.get('href',None)
        print('href=',href)
        url2 = href
        html2 = urllib.request.urlopen(url2, context=ctx).read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        tags = soup2('a')
        req_tag2 = tags[position]
        return access_links(req_tag2, count,position)


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Meenal.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter the count'))
position = int(input('Enter the position'))

tags = soup('a')
req_tag = tags[position]
access_links(req_tag, count, position)


