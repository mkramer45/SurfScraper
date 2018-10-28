from lxml import html
import requests

page = requests.get('https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/')
tree = html.fromstring(page.content)


#This will create a list of buyers:
intervals = tree.xpath('//*[@class="nomargin font-sans-serif heavy"]/text()')

print(intervals)


