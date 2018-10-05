from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

fruits = [
    {'id': 1, 'title': 'apple', 'price': 1.2},
    {'id': 2, 'title': 'banana', 'price': 2.1},
    {'id': 3, 'title': 'orange', 'price': 1.7},
]

@app.route("/")
def index():
    return "Hello World"


@app.route("/api/fruits", methods=['GET'])
def get_fruits():
    return jsonify({'data': fruits})

@app.route("/api/fruit", methods=['POST'])
def get_fruit():
    if not request.json or not 'id' in request.json:
        abort(400)

    id = int(request.json['id'])
    result = {}
    for fruit in fruits:
        if fruit['id'] == id:
            result = fruit
    return jsonify({'data': result}), 201



if __name__ == "__main__":
    app.run(debug=False)

