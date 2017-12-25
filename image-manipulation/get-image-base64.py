import sys
import bs4
import base64
import urllib
import urllib3

HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
SEARCH_URL = "https://www.google.de/search?tbm=isch&q="
TNB_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:"
urllib3.disable_warnings()
http = urllib3.PoolManager()


def extract_url(anchor):
    url = anchor.get('data-src')
    if url:
        return url
    else:
        name = anchor.get('name')
        if name is None:
            sys.stderr.write('extract_url needs to be updated')
            sys.exit(2)
        return TNB_URL + name


def get_urls(query):
    r = http.request('GET', SEARCH_URL + urllib.parse.quote(query), headers=HEADERS)
    if r.status != 200:
        sys.stderr.write(query)
        sys.stderr.write(r.status)
        sys.exit(1)
    soup = bs4.BeautifulSoup(r.data, 'html.parser')
    return [extract_url(a) for a in soup.find_all("img", attrs={'class': 'rg_ic rg_i'})]


def getImageData(url):
    r = http.request('GET', url, headers=HEADERS)
    if r.status != 200:
        sys.stderr.write(url)
        sys.stderr.write(r.status)
        sys.exit(1)
    return r.data


def print_base64(query, count):
    urls = get_urls(query)
    urls = urls[:count]
    for url in urls:
        print("data:image;base64," + str(base64.b64encode(getImageData(url)))[2:-1])


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("example: python3 get-image-base64.py Apfel 4")
    else:
        print_base64(sys.argv[1], int(sys.argv[2]))
