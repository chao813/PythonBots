from bs4 import BeautifulSoup
import urllib

response = urllib.urlopen('http://www.google.com/')
doc = response.read()

soup = BeautifulSoup(doc)

for link in soup.find_all('a'):
    print(link.get('href'))

