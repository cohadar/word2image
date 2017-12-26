from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/word/<word>', methods=['GET'])
def get_image_by_word(word):
    return jsonify({'word': word, 'weight': 0, 'text': '', 'imgs': []})

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
