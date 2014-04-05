import os, sys; sys.path.append(os.path.join("..", "..", ".."))

from pattern.web   import Newsfeed, plaintext, URL
from pattern.table import date

wsj    = "http://online.wsj.com/xml/rss/3_7014.xml"

engine = Newsfeed()

for result in engine.search(wsj, cached=True):
    print result.title.upper()
    print plaintext(result.description) # Remove HTML formatting.
    print result.url
    print result.date
    print


