import sys

#Check for beauifull soup installation
try:
    import BeautifulSoup
except ImportError:
    sys.exit("""You need Beautiful Soup ! install it from http://pypi.python.org/pypi/foo or run pip install foo.""")

#Check for requests installation
try:
    import requests
except ImportError:
    sys.exit("""You need request package installd ! """)

#check for urllib2 installation
try:
    import urllib2
except ImportError:
    sys.exit("""You need urllib2 package installd ! """)

import urllib2
import requests
from BeautifulSoup import BeautifulSoup

# selector function return list of movies having music rating > 3.5
def  selector(url):
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)

    #print soup.prettify()
    header = soup.findAll('div', attrs={'class': 'movreviewwblock mht203 mfl mml9 minline'})

    result = []

    dict = {};

    counter = 0

    for div in header:
            movie = ""
            rating = 0

            links = div.findAll('img')

            for a in links:
                if counter == 0 :
                    movie = a['title']
                if counter == 2:
                    rating = float(a['alt'])
                if rating >= 3.5 :
                    result.append(movie)
                counter = counter+1

            counter = 0
    return result

#This function download songs of the movie
def download(downloadList):
    for movie in downloadList:
        print "Need to download songs of :"+movie

downloadList = selector("http://www.bollywoodhungama.com/more/musicreviews")

download(downloadList)


