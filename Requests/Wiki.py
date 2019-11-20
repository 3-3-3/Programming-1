import requests   
from bs4 import BeautifulSoup as soup
import random 


target = 'Dog'
base_url = 'https://en.wikipedia.org/wiki/'
s = requests.Session()

def find_target(url, target, paths=[]):
	p = paths
	p.append(url)
	r = s.get(url, verify=False, allow_redirects=False)
	links = []
	parser = soup(r.text)
	for i in parser.find_all('a'):
		link = str(i.get('href'))
		if (link[:5] == '/wiki') and (':' not in link) and ('%' not in link):
			links.append(link)

	for i in links:
		if i[6:] == target:
			p.append(i)
			return p
	
	rand = random.randint(0, len(links)-1)
	print(links[rand])
	return find_target(base_url + links[rand], target, p)


'''paths = find_target(base_url + 'Dog', 'Tesla_(unit)')
print(paths)'''

req = requests.get(base_url + 'Dog')
pars = soup(req.text)
for i in pars.find_all('a'):
	print(i.get('href'))
	
