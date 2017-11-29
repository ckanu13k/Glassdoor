import urllib.request, sys #urllib2, sys
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
import json

url = "http://api.glassdoor.com/api/api.htm?t.p=25738&t.k=iRCtcWJQamE&format=json&v=1&action=employers&q="
url = "http://api.glassdoor.com/api/api.htm?t.p=215589&t.k=v4PiKudaNW&format=json&v=1&action=employers&l=Houston,%20TX&pn=30&q="
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url,headers=hdr) #urllib2.Request(url,headers=hdr)
response = urllib.request.urlopen(req)
soup = BeautifulSoup(response, "lxml")
#soup = BeautifulSoup(response)
#print(soup.prettify()[1:1])


letters = ''.join(text for text in soup.p.find_all(text=True, recursive=False))

#print(letters)
with open('glassdoor.txt', 'w') as outfile:
    json.dump(letters, outfile)

with open('glassdoor.txt', 'r') as f:
     data = json.load(f)

print("Printing loaded *.json file!!!!!!!!!!!")
print(data)
