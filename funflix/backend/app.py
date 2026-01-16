from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Miniflix Backend!"})

@app.route('/movies')
def movies():
    return jsonify([
        {"id": 1, "title": "Movie 1"},
        {"id": 2, "title": "Movie 2"},
        {"id": 3, "title": "Movie 3"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

