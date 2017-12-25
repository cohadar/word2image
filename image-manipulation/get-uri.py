from bs4 import BeautifulSoup
from os import path
import requests, re, urllib2, os, cookielib, json, sys

header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def get_uris(query, cnt):
    url = "https://www.google.de/search?tbm=isch&q=" + query    
    soup = get_soup(url,header)
    
    for a in soup.find_all("img", attrs ={'class':'rg_ic rg_i'}):
        url = a.get('data-src')
        if url:
            print url
            cnt = cnt - 1
        if cnt <= 0:
            break

if len(sys.argv) == 1:
    print "usage:   <word> [<count>]"
    print "example: get-uri.py Apfel 5"
elif len(sys.argv) == 2:
    get_uris(sys.argv[1], 4)
else:
    get_uris(sys.argv[1], int(sys.argv[2]))
