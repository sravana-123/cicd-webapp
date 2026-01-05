from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask Backend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
