#!/usr/bin/python3

# ./pagecheck.py https://www.postaonline.cz/en/trackandtrace/-/zasilka/cislo?parcelNumbers=LF8526717832F#LF8526717832F-detail table class datatable2 

import requests
import sys
import hashlib

from html.parser import HTMLParser
from bs4 import BeautifulSoup

url = sys.argv[1]
element = sys.argv[2]
attr = sys.argv[3]
value = sys.argv[4]

r = requests.get(url)

body = r.text

soup = BeautifulSoup(body, 'html.parser')

attrs = {
    attr: value
    }

track = soup.find_all(element, attrs=attrs)

print(hashlib.md5(track.__str__().encode('utf-8')).hexdigest())

