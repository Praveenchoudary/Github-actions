from flask import Flask, request, jsonify
from app.calculator import add, subtract

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'result': add(a, b)})

@app.route('/subtract')
def subtract_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'result': subtract(a, b)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
