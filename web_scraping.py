from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
    
    title = getTitle(url)
    if title == None:
      return "Title could not be found"
    else:
      return title

print(getTitle("https://www.google.com/search?q=face&oq=face&aqs=chrome..0j69i57j0l6.3850j0j7&sourceid=chrome&ie=UTF-8"))
print(getTitle("http://www.facebook.com/"))