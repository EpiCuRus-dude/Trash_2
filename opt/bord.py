import numpy as np

Scores = np.random.randint(50, 100, size=(10, 3, 4))  # Random scores



borda_points = np.zeros(num_candidates)

for test in range(num_tests):
    for ref in range(num_refs):
        scores = Scores[test, :, ref]
        
        
        ranks = np.argsort(scores)[::-1]  # Descending order
        

        for i, candidate in enumerate(ranks):
            borda_points[candidate] += (num_candidates - i)  # Points assignment

final_winner = np.argmax(borda_points)  # Overall winner
final_ranking = np.argsort(borda_points)[::-1]  # Final ranking

print("Borda Points for Each Candidate:", borda_points)
print("Overall Winner (Index):", final_winner)
print("Final Candidate Ranking (Indices):", final_ranking)


candidate_names = ["Alice", "Bob", "Charlie"]  # Adjust as needed

final_ranking_named = [candidate_names[i] for i in final_ranking]

print("Final Candidate Ranking (Named):", final_ranking_named)
print("Overall Winner (Named):", candidate_names[final_winner])
