#from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2
import re

inputFormat = re.compile("^http[s]*://.+\..+$")

#get the input domain from the user, do some basic validation on it
while 1:
	domainToCrawl = raw_input('Please enter a domain to crawl for quotes (e.g. http://stackoverflow.com) : ')
	if inputFormat.match(domainToCrawl):
		break

#To Do:
#get the page, all internal links add to internal links hash


#get a random URL from the toVisit hash, get that page
#add the URL to the visitedPages hash
#check each internal URL against the visitedPages hash before adding it to the toVisit hash


#http://docs.python.org/2/library/urlparse.html

response = urllib2.urlopen(domainToCrawl)
pageSrc = response.read()

print pageSrc

#response = urllib2.urlopen("http://google.de")
#page_source = response.read()
