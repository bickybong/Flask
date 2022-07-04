from flask import Flask, jsonify

app = Flask(__name__)

items = [2,5,2,3]

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/items")
def iitems():
    return jsonify(items=items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')