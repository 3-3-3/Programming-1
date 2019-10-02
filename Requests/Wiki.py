import requests   
from bs4 import BeautifulSoup as soup


target = 'Dog'
s = requests.Session()

def find_target(url):
	r = s.get(url, verify=False)
	links = []
	parser = soup(r.text)
	for i in parser.find_all('a'):
		link = str(i.get('href'))
		print(link[:5])
		if (link[:5] == '/wiki') and (':' not in link):
			links.append(link)

	for i in links:
		print(i)
