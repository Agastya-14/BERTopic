from bertopic import BERTopic
import json

# Load dataset
with open("data/al_baqarah.json", "r", encoding="utf-8") as f:
    docs = [d["text"] for d in json.load(f)]

# Buat dan latih model BERTopic
topic_model = BERTopic()
topics, probs = topic_model.fit_transform(docs)

# Reduce jumlah topik jadi 5
topic_model = topic_model.reduce_topics(docs, nr_topics=5)

# Simpan model
topic_model.save("bertopic_model")

print("Model BERTopic selesai dilatih dan disimpan dengan 5 topik.")
