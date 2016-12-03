import urllib
from BeautifulSoup import *

url = raw_input("enter url")
count = (int)(raw_input("enter count"))
pos = (int)(raw_input("enter position"))
i = 0
while True:
 if (i <= count):
	print  "Retrieving" + url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	url = tags[pos-1].get('href',None)
	i = i + 1
 else:
	break   