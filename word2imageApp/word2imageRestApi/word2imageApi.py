from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import redis
import sys
import bs4
import urllib
import urllib3
import os
import base64

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PASS = os.environ['REDIS_PASS']

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
            return None
        return TNB_URL + name

def get_urls(query):
    r = http.request('GET', SEARCH_URL + urllib.parse.quote(query), headers=HEADERS)
    if r.status != 200:
        sys.stderr.write(r.status)
        return None
    soup = bs4.BeautifulSoup(r.data, 'html.parser')
    return [extract_url(a) for a in soup.find_all("img", attrs={'class': 'rg_ic rg_i'})]

def getImageData(url):
    r = http.request('GET', url, headers=HEADERS)
    if r.status != 200:
        sys.stderr.write(url)
        sys.stderr.write(r.status)
        return None
    return r.data

app = Flask(__name__)

redis_db = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0, password=REDIS_PASS)

@app.route('/search', methods=['GET'])
def get_image_by_word():
    word = request.args.get('q', default='', type=str)
    if not word:
        return Response("{}", status=404, mimetype='application/json')
    weight = redis_db.get("WORD:" + word)
    if weight:
        weight.decode('utf-8')
        weight = int(weight)
    else:
        weight = 0
    text = redis_db.get("TEXT:" + word)
    if text:
        text.decode('utf-8')
        text = str(text)
    else:
        text = ''
    imgs = redis_db.lrange("IMGS:" + word, 0, 3)
    images = []
    for i in imgs:
        images.append(str(i.decode('utf-8')))
    if weight == 0 and text == '' and len(images) == 0:
        return Response("{}", status=404, mimetype='application/json')
    return jsonify({'word': word, 'weight': weight, 'text': text, 'imgs': images})

@app.route('/appendimg/<word>', methods=['POST'])
def insert_word_2_image(word):
    data = request.get_json()
    if not data['url']:
        return Response("{}", status=404, mimetype='application/json')
    img = getImageData(data['url'])
    if not img:
        return Response("{}", status=404, mimetype='application/json')
    image = base64.b64encode(img).decode('utf-8')
    image = 'data:image;base64,' + image
    if redis_db.llen("IMGS:" + word) >= 4:
        redis_db.lpop("IMGS:" + word)
    redis_db.rpush("IMGS:" + word, image)
    return Response("{}", status=200, mimetype='application/json')

@app.route('/searchurls', methods=['GET'])
def searchImages():
    query = request.args.get('q', default='', type=str)
    if not query:
        return Response("{}", status=404, mimetype='application/json')
    urls = get_urls(query)
    if urls:
        return jsonify({'urls': urls})
    else:
        return Response("{}", status=404, mimetype='application/json')

@app.route('/rotateimgs/<word>', methods=['POST'])
def rotateimgs(word):
    if not word:
        return Response("{}", status=404, mimetype='application/json')
    img = redis_db.rpoplpush("IMGS:" + word, "IMGS:" + word)
    if img:
        return Response("{}", status=200, mimetype='application/json')
    else:
        return Response("{}", status=404, mimetype='application/json')

@app.route('/deleteimg/<word>/<index>', methods=['DELETE'])
def deleteImage(word, index):
    if not word:
        return Response("{}", status=404, mimetype='application/json')
    if int(index) < 0 or int(index) > 3:
        return Response("{}", status=404, mimetype='application/json')
    redis_db.lset("IMGS:" + word, index, "DELETEME")
    redis_db.lrem("IMGS:" + word, 4, "DELETEME")
    return Response("{}", status=200, mimetype='application/json')

@app.route('/updateText/<word>', methods=['PUT'])
def updateText(word):
    if not word:
        return Response("{}", status=404, mimetype='application/json')
    data = request.get_json()
    if not data['text']:
        return Response("{}", status=404, mimetype='application/json')
    redis_db.set("TEXT:" + word, data['text'])
    return Response("{}", status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
