import pyshorteners as sh
from flask import Flask, request, jsonify

app = Flask(__name__)


# Default API
@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        data = {"data": "Hello World"}
        return jsonify(data)


# Encodes a URL to a shortened  URL
@app.route('/encode', methods=['GET', 'POST'])
def encode_url():
    input_data = request.json
    link = input_data['link']
    s = sh.Shortener()
    x = (s.tinyurl.short(link))
    return x


# Decodes a shortened URL to its original URL.
@app.route('/decode', methods=['GET', 'POST'])
def decode_url():
    input_data = request.json
    link = input_data['link']
    s = sh.Shortener()
    x = s.tinyurl.expand(link)
    return x


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

