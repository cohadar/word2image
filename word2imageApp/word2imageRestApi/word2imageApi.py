from flask import Flask
from flask import jsonify
from flask import request
import redis

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
    imgs = redis_db.get("LRANGE:" + word + "0 3")
    images = []
    if(imgs):
        images.append(str(imgs[0].decode('utf-8')))
        images.append(str(imgs[1].decode('utf-8')))
        images.append(str(imgs[2].decode('utf-8')))
        images.append(str(imgs[3].decode('utf-8')))
    return jsonify({'word': word, 'weight': weight, 'text': text, 'imgs': images})

@app.route('/nextUnprocessedWord', methods=['GET'])
def get_next_unprocessed_word():
    return jsonify({'nextWord': 'word'})

@app.route('/word2image', methods=['POST'])
def insert_word_2_image():
    data = request.get_json()
    result =  word2image(data['word'], data['translate'], data['image1'], data['image2'], data['image3'], data['image4'])
    return jsonify({'result': 'done'})

if __name__ == '__main__':
    app.run(debug=True)
