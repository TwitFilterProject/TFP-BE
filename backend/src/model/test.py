import sys
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/test', methods=['POST'])

def test():
    data = request.json
    text = data['body']
    print(text)
    return jsonify(text + '??') 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)