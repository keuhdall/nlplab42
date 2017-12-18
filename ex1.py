import embeddings

emb = embeddings.EmbeddingsDictionary(100000)
print(emb.w2neighbors("geek", 10))