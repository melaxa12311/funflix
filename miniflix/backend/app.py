from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/movies")
def movies():
    return jsonify([
        {"name": "Movie 1"},
        {"name": "Movie 2"},
        {"name": "Movie 3"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

