from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page2.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)

# pg10 - Connecting Reliably and Handling Exceptions