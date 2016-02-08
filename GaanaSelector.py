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
                if(counter == 0):
                    movie = a['title']

                if(counter == 2):
                    rating = float(a['alt'])
                    print "Rating is",rating

                if(rating >= 3.5):
                    result.append(movie

                counter = counter+1
            counter = 0
    return result

print selector("http://www.bollywoodhungama.com/more/musicreviews")

