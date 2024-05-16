import numpy as np
import matplotlib.pyplot as plt

def find_elbow_point(scores):
    # Step 1: Sort the scores in descending order along with their original indices
    sorted_indices_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    sorted_indices, sorted_scores = zip(*sorted_indices_scores)
    
    # Step 2: Compute the cumulative sum
    cumulative_sum = np.cumsum(sorted_scores)
    
    # Step 3: Normalize by the total score
    total_score = cumulative_sum[-1]
    cumulative_percentage = cumulative_sum / total_score * 100
    
    # Step 4: Find the elbow point
    x = np.arange(1, len(scores) + 1)
    y = cumulative_percentage
    
    # Plot the cumulative percentage
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Candidates')
    plt.ylabel('Cumulative Percentage of Total Score')
    plt.title('Elbow Method to Determine Top Candidates')
    plt.grid(True)
    plt.show()
    
    # Use the "elbow" point heuristic
    elbow_point = np.argmax(np.diff(y, 2)) + 1
    
    # Get the indices of the top candidates
    top_candidate_indices = sorted_indices[:elbow_point]
    
    return elbow_point, top_candidate_indices

# Example usage
scores = [10, 50, 20, 30, 40, 60, 70, 80, 90, 100]
elbow_point, top_candidate_indices = find_elbow_point(scores)

print(f"The number of top candidates to choose: {elbow_point}")
print(f"Indices of the top candidates: {top_candidate_indices}")
