from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

class word2image(object):
    def __init__(self, word, translate, image1, image2, image3, image4):
        super(word2image, self).__init__()
        self.word = word
        self.translate = translate
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4


@app.route('/word/<word>', methods=['GET'])
def get_image_by_word(word):
    result = word2image(word, 'translate', 'image1', 'image2', 'image3', 'image4')
    return jsonify({'word': result.word, 'translate': result.translate,
    'image1': result.image1, 'image2': result.image2, 'image3': result.image3, 'image4': result.image4})

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
