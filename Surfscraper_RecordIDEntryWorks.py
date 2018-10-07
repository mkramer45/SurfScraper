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
	date = page_soup.findAll('th', class_=re.compile("row-title background-gray-lighter"))
	#DB creation
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS SurfDate(ID INTEGER PRIMARY KEY AUTOINCREMENT, Day TEXT)')

# iterates over parsed HTML
	# for wave in wavez:
	# 	#1 wavesize
	# 	wavesize = wave.find('li', class_='rating-text text-dark')
	# 	wavesizex = wavesize.text.strip()
		#2 summary
	# for d in date:
	# 	datex = d.find('h6', class_='nomargin pull-left heavy table-header-title').get_text()
	e = 't'


	print(e)
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	#cursor.execute("INSERT INTO SurfDate VALUES (?)", (e))
	cursor.execute("INSERT INTO SurfDate (Day) VALUES (?)", (e,))
	#cursor.execute("INSERT INTO SurfDate VALUES (?,?)", (id, datex))
	conn.commit()
	cursor.close()
	conn.close()