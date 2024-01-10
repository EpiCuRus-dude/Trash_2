def normalize_vectors(vectors):
    
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / norms
