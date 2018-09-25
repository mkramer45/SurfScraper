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

my_url = ['https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/', 
'https://magicseaweed.com/2nd-Beach-Sachuest-Beach-Surf-Report/846/','https://magicseaweed.com/Nahant-Surf-Report/1091/',
'https://magicseaweed.com/Nantasket-Beach-Surf-Report/371/',
'https://magicseaweed.com/Scituate-Surf-Report/372/',
'https://magicseaweed.com/Cape-Cod-Surf-Report/373/',
'https://magicseaweed.com/The-Wall-Surf-Report/369/',
'https://magicseaweed.com/Green-Harbor-Surf-Report/864/',
'https://magicseaweed.com/Cape-Ann-Surf-Report/370/',
'https://magicseaweed.com/27th-Ave-North-Myrtle-Surf-Report/2152/',
'https://magicseaweed.com/Cocoa-Beach-Surf-Report/350/'
]
# opening up connecting, grabbing the page

for url in my_url:

	uClient = uReq(url)
# this will offload our content in'to a variable
	page_html = uClient.read()
# closes our client
	uClient.close()

# html parsing
	page_soup = soup(page_html, "html.parser")

	wavez = page_soup.findAll('div', class_=re.compile("col-lg-7 col-md-7 col-sm-7 col-xs-12"))
	beaches = page_soup.findAll('div', class_=re.compile("fluid-column"))
	desc = page_soup.findAll('div', class_=re.compile("list-group-title"))

	print(url)
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS Tracks(WaveSize TEXT, Beach TEXT, WebSource TEXT, Summary TEXT)')


# MSK, artist name
	for wave in wavez:

		wavesize = wave.find('li', class_='rating-text text-dark')
		wavesizex = wavesize.text.strip()

		web_src = 'Magic_Seaweed'

		for beach in beaches:

			beachname = beach.find('h1', class_='nomargin page-title')
			beachnamex = beachname.text.strip()

			for d in desc:
				summary = d.find('div', class_='inline-block')


			print(wavesizex)

			conn = sqlite3.connect('SurfSend.db')
			cursor = conn.cursor()
			cursor.execute("INSERT INTO Tracks VALUES (?, ?, ?, ?)", (wavesizex, beachnamex, web_src, summary))
			conn.commit()
			cursor.close()
			conn.close()