

This script requires that beautifulsoup is installed.  To install this, run apt-get install python-bs4 .

This script is similar to some things I had to build at an old job, although those scripts were written in PHP using the simple_html_dom.php library, and then later on I rewrote them to use the QueryPath library(too many memory leaks in simple_html_dom.php for the size sites I was crawling).  I also wrote similar crawling scripts using Perl, WWW::Mechanize, URI::http and Text::CSV to crawl inputted spreadsheets looking for certain things on pages.
