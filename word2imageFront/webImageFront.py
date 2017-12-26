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

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
def root():
   return app.send_static_file('researchData.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
