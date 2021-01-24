from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/test")
def test():
    return jsonify({"status": "OK"}), 200
