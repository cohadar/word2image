from bs4 import BeautifulSoup
from os import path
import requests, re, urllib2, os, cookielib, json, sys

header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def download_images(query, cnt):
    print("Get images for " + query)
    url = "https://www.google.de/search?tbm=isch&q=" + query    
    soup = get_soup(url,header)
    
    images = []
    for a in soup.find_all("img", attrs ={'class':'rg_ic rg_i'}):
        url = a.get('data-src')
        if url:
            images.append(url)

    for i, url in enumerate(images[:cnt]):
        print "downloading " + url
        f = urllib2.urlopen(url)

        folder = os.path.join('pic', query)
        if not os.path.exists(folder):
            os.makedirs(folder)    

        with open(folder + "/" + str(i) + ".jpg", "wb") as local_file:
                local_file.write(f.read())

words = []
for line in sys.stdin:
    w = line.split()[1]
    download_images(w, 4)
