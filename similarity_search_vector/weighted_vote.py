from scipy.special import softmax

def predict_category_weighted(new_title, k=5):
    new_vector = vectorizer.transform([new_title]).toarray().astype(np.float32)
    distances, indices = index.search(new_vector, k=k)

    
    weights = 1 / (1 + distances[0])  
    weights = softmax(weights)  

    
    weighted_category_votes = {}
    for idx, weight in zip(indices[0], weights):
        category = categories[idx]
        weighted_category_votes[category] = weighted_category_votes.get(category, 0) + weight

    most_common_category = max(weighted_category_votes, key=weighted_category_votes.get)
    return most_common_category


predicted_category = predict_category_weighted(new_title, k=5)
print(f"The predicted category for '{new_title}' is {predicted_category}")
