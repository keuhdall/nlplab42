import embeddings

emb = embeddings.EmbeddingsDictionary(100000)

def analogy(self, w1, w2, w3):
    i1 = self.dictionary[w1]
    i2 = self.dictionary[w2]
    i3 = self.dictionary[w3]

    target_embedding = self.emb[i1] + self.emb[i2] - self.emb[i3]
    _scores, closest_word_index = self.emb2neighbors(target_embedding, top_k=20)
    for ind in closest_word_index:
        print(self.words[ind])
    
analogy(emb, 'france', 'croissant', 'wine')