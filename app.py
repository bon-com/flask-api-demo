import os
from flask import Flask, jsonify, request

app = Flask(__name__)


# ルートエンドポイント
@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask API!"})


# ヘルスチェック用エンドポイント
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# テキストをそのまま返すエコーエンドポイント
@app.route("/echo")
def echo():
    text = request.args.get("text", "")
    return jsonify({"echo": text})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
