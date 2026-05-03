from flask import Flask, render_template, request
from bertopic import BERTopic
import json

app = Flask(__name__)

# Load dataset
with open("data/al_baqarah.json", "r", encoding="utf-8") as f:
    docs = [d["text"] for d in json.load(f)]

# Load model
topic_model = BERTopic.load("bertopic_model")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    # Ambil jumlah topik dari input user
    nr_topics = int(request.form["nr_topics"])

    # Reduce topik sesuai input
    reduced_model = topic_model.reduce_topics(docs, nr_topics=nr_topics)

    topics = []
    for topic_id in reduced_model.get_topics():
        words = reduced_model.get_topic(topic_id)
        # Filter: hanya tampilkan topik dengan kata bermakna
        if words and any(weight > 0.0001 for _, weight in words):
            topics.append({"id": topic_id, "words": words})

    return render_template("result.html", topics=topics)

if __name__ == "__main__":
    app.run(debug=True)
