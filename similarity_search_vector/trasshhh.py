import numpy as np
import matplotlib.pyplot as plt

def find_sugs_elbow_point(scores, alpha=0.05):
    # Step 1: Sort the scores in descending order along with their original indices
    sorted_indices_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    sorted_indices, sorted_scores = zip(*sorted_indices_scores)
    
    # Step 2: Compute the cumulative sum
    cumulative_sum = np.cumsum(sorted_scores)
    
    # Step 3: Normalize by the total score
    total_score = cumulative_sum[-1]
    cumulative_percentage = cumulative_sum / total_score * 100
    
    # Step 4: Detect change points using SUGS
    change_points = []
    for i in range(1, len(cumulative_percentage)):
        if cumulative_percentage[i] - cumulative_percentage[i-1] < alpha * cumulative_percentage[i-1]:
            change_points.append(i)
    
    # Select the first significant change point as the elbow point
    elbow_point = change_points[0] if change_points else len(scores)
    
    # Ensure at least one candidate is selected
    if elbow_point == 0:
        elbow_point = 1
    
    # Plot the cumulative percentage with the elbow point
    x = np.arange(1, len(scores) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(x, cumulative_percentage, marker='o', label='Cumulative Percentage')
    plt.axvline(x=elbow_point, color='r', linestyle='--', label='Elbow Point')
    plt.xlabel('Number of Candidates')
    plt.ylabel('Cumulative Percentage of Total Score')
    plt.title('SUGS Method to Determine Top Candidates')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Get the indices of the top candidates
    top_candidate_indices = sorted_indices[:elbow_point]
    
    return elbow_point, top_candidate_indices

# Example usage
scores = [10, 50, 20, 30, 40, 60, 70, 80, 90, 100]
elbow_point, top_candidate_indices = find_sugs_elbow_point(scores, alpha=0.05)

print(f"The number of top candidates to choose: {elbow_point}")
print(f"Indices of the top candidates: {top_candidate_indices}")
