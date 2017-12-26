from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import redis
import sys
import bs4
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
        sys.stderr.write(r.status)
        sys.exit(1)
    soup = bs4.BeautifulSoup(r.data, 'html.parser')
    return [extract_url(a) for a in soup.find_all("img", attrs={'class': 'rg_ic rg_i'})]

app = Flask(__name__)

redis_db = redis.StrictRedis(host="iv.hackaton.tda.link", port=6379, db=0, password='svebisekeljubilemornare')

@app.route('/word/<word>', methods=['GET'])
def get_image_by_word(word):
    weight = redis_db.get("WORD:" + word)
    weight.decode('utf-8')
    weight = int(weight)
    text = redis_db.get("TEXT:" + word)
    text.decode('utf-8')
    text = str(text)
    imgs = redis_db.lrange("IMGS:" + word, 0, 3)
    images = []
    if(imgs):
        images.append(str(imgs[0].decode('utf-8')))
        images.append(str(imgs[1].decode('utf-8')))
        images.append(str(imgs[2].decode('utf-8')))
        images.append(str(imgs[3].decode('utf-8')))
    return jsonify({'word': word, 'weight': weight, 'text': text, 'imgs': images})

@app.route('/appendimg/<word>', methods=['POST'])
def insert_word_2_image():
    data = request.get_json()
    result =  word2image(data['word'], data['translate'], data['image1'], data['image2'], data['image3'], data['image4'])
    return jsonify({'result': 'done'})

@app.route('/searchurls/<query>', methods=['GET'])
def searchImages(query):
    urls = get_urls(query)
    return jsonify({'urls': urls})

@app.route('/rotateimgs/<word>', methods=['POST'])
def rotateimgs(word):
    img = redis_db.rpoplpush("IMGS:" + word, "IMGS:" + word)
    if img:
        return Response("{}", status=200, mimetype='application/json')
    else:
        return Response("{}", status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
