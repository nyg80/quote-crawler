from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
import urllib2
import re

inputFormat = re.compile("^http[s]*://.+\..+$")


#using dictionaries which act like hashes, so that the key will contain our lowercase, full-length
#URL and the value will contain the (potentially mixed-case) URL we found on the page
#this way, we can makes requests for mixed case URLs so that IIS servers won't 404 on us unnecessarily
toVisit = {}
visitedPages = {}

#get the input domain from the user, do some basic validation on it
while 1:
	domainToCrawl = raw_input('Please enter a domain to crawl for quotes (e.g. http://stackoverflow.com) : ')
	if inputFormat.match(domainToCrawl):
		break

#To Do: make URL comparisons case insensitive, but keep requested URLs mixed-case so that IIS servers dont give 404s on us


#get the page, all internal links add to internal links hash
response = urllib2.urlopen(domainToCrawl)
pageSrc = response.read()

soup = BeautifulSoup(pageSrc)

while True:
	#text extraction & analysis portion of code
	pText = soup.find_all('p').getText()

	#crawling portion of code
	for link in soup.find_all('a'):
		#convert relative links to absolute links, so we can determine internal vs external links
		if link.get('href') is not None:
			if link.get('href').startswith("/"):
				linkAddr = domainToCrawl + link.get('href')
			else:
				linkAddr = link.get('href')
			if domainToCrawl in linkAddr:
				if (linkAddr not in visitedPages) and (not linkAddr.endswith(".pdf")):
					toVisit[linkAddr] = link.get('href')
					#print "added %s to toVisit" % linkAddr
	nextPage = toVisit.popitem()
	soup = BeautifulSoup(urllib2.urlopen(nextPage[0]).read())
	visitedPages[nextPage[0]] = nextPage[1]
	if not toVisit:
		break

print visitedPages

#links = soup.find_all('a')

#print links



#get a random URL from the toVisit hash, get that page
#add the URL to the visitedPages hash
#check each internal URL against the visitedPages hash before adding it to the toVisit hash


#http://docs.python.org/2/library/urlparse.html



#print pageSrc

#response = urllib2.urlopen("http://google.de")
#page_source = response.read()
