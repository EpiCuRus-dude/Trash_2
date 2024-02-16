embeddings = embeddings / np.linalg.norm(embeddings, axis=1)[:, np.newaxis]
