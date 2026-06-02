from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Loading dataset
df = pd.read_csv("data/data.csv")
@app.route("/")
def home():
    return "Book API Running."

@app.route("/books")
def get_books():
    return jsonify(df.to_dict(orient="records"))

@app.route("/top")
def top_books():
    top = df.sort_values(by="PRICE", ascending=False).head(10)
    return jsonify(top.to_dict(orient="records"))
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
