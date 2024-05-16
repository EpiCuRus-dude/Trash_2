import numpy as np
import matplotlib.pyplot as plt

def find_strict_elbow_point(scores):
    # Step 1: Sort the scores in descending order along with their original indices
    sorted_indices_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    sorted_indices, sorted_scores = zip(*sorted_indices_scores)
    
    # Step 2: Compute the cumulative sum
    cumulative_sum = np.cumsum(sorted_scores)
    
    # Step 3: Normalize by the total score
    total_score = cumulative_sum[-1]
    cumulative_percentage = cumulative_sum / total_score * 100
    
    # Step 4: Calculate the rate of change
    rate_of_change = np.diff(cumulative_percentage)
    
    # Determine an automatic threshold for strict selection
    mean_rate = np.mean(rate_of_change)
    std_rate = np.std(rate_of_change)
    threshold = mean_rate - std_rate  # Using mean - std as a stricter threshold

    # Find the point where the rate of change falls below the threshold
    elbow_point = np.argmax(rate_of_change < threshold) + 1
    
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
    plt.title('Strict Elbow Method to Determine Top Candidates')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Get the indices of the top candidates
    top_candidate_indices = sorted_indices[:elbow_point]
    
    return elbow_point, top_candidate_indices

# Example usage
scores = [10, 50, 20, 30, 40, 60, 70, 80, 90, 100]
elbow_point, top_candidate_indices = find_strict_elbow_point(scores)

print(f"The number of top candidates to choose: {elbow_point}")
print(f"Indices of the top candidates: {top_candidate_indices}")
