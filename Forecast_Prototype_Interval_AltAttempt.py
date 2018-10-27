import bs4
import requests
from bs4 import BeautifulSoup as soup
import sqlite3
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#list of URLs to scrape from
my_url = ['https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/']
# opening up connecting, grabbing the page

#iterate over list of URLS
for url in my_url:
	#initiating python's ability to parse URL
	uClient = uReq(url)
# this will offload our content in'to a variable
	page_html = uClient.read()
# closes our client
	uClient.close()

# html parsing
	#beautifulsoup magic
	page_soup = soup(page_html, "html.parser")
	#master div class where our li class value is stored
	wavez = page_soup.findAll('td', class_=re.compile("text-center background-gray-lighter"))

# iterates over parsed HTML
	for wave in wavez:
		#drilling down within our master class to the explicit li class where our data lives
		wavesize = wave.find('h4', class_='nomargin font-sans-serif heavy')
		wavesizex = wavesize.text.strip()
		if wavesizex.endswith('ft'):
			waveheight = wavesizex
		elif wavesizex.endswith('s'):
			waveint = wavesizex

		print(wavesize)
