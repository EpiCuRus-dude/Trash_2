import numpy as np
import matplotlib.pyplot as plt

def find_optimal_candidates(scores):
    # Step 1: Sort the scores in descending order along with their original indices
    sorted_indices_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    sorted_indices, sorted_scores = zip(*sorted_indices_scores)
    
    # Determine the number of top candidates using the 1/e law
    n = len(scores)
    top_candidates_count = int(np.ceil(n / np.e))
    
    # Ensure at least one candidate is selected
    top_candidates_count = max(1, top_candidates_count)
    
    # Plot the sorted scores with the cutoff point
    x = np.arange(1, n + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(x, sorted_scores, marker='o', label='Sorted Scores')
    plt.axvline(x=top_candidates_count, color='r', linestyle='--', label='Cutoff Point')
    plt.xlabel('Number of Candidates')
    plt.ylabel('Scores')
    plt.title('Top Candidates Selection')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Get the indices of the top candidates
    top_candidate_indices = sorted_indices[:top_candidates_count]
    
    return top_candidates_count, top_candidate_indices

# Example usage
scores = [10, 50, 20, 30, 40, 60, 70, 80, 90, 100]
top_candidates_count, top_candidate_indices = find_optimal_candidates(scores)

print(f"The number of top candidates to choose: {top_candidates_count}")
print(f"Indices of the top candidates: {top_candidate_indices}")
