from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # title = bs.head.title.text
        title = bs.body.h1.text
    except AttributeError as e:
        return None
    return title

title = getTitle('http://pythonscraping.com/pages/page2.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
# pg10 - Connecting Reliably and Handling Exceptions