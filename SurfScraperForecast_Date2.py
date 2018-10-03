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
	#variable for soon to be parsed page
	wavez = page_soup.findAll('div', class_=re.compile("col-lg-7 col-md-7 col-sm-7 col-xs-12"))
	desc = page_soup.findAll('div', class_=re.compile("list-group-content"))
	swell = page_soup.findAll('td', class_=re.compile("text-center background-gray-lighter"))
	date = page_soup.findAll('th', class_=re.compile("row-title background-gray-lighter"))

	#DB creation
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS SurfReport(WaveSize TEXT, WaveInterval TEXT, Day TEXT)')

# iterates over parsed HTML
	for d in date:
		#1 wavesize
		datex = d.find('h6', class_='nomargin pull-left heavy table-header-title').get_text()

		#scraping wave height & interval
	for w in swell:
		swellx = w.find('h4', class_='nomargin font-sans-serif heavy')
		swelly = swellx.text.strip()
		if swelly.endswith('ft'):
			swelly2 = swelly
		elif swelly.endswith('s'):
			swelly3 = swelly
			for d in date:
				#1 wavesize
				datex = d.find('h6', class_='nomargin pull-left heavy table-header-title').get_text()

				conn = sqlite3.connect('SurfSend.db')
				cursor = conn.cursor()
				cursor.execute("INSERT INTO SurfReport VALUES (?,?,?)", (swelly2, swelly3, datex))
				conn.commit()
				cursor.close()
				conn.close()