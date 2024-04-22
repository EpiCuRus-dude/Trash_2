import numpy as np

Scores = np.random.randint(50, 100, size=(10, 3, 4))  # Random scores


num_tests, num_candidates, num_refs = Scores.shape


winners = np.zeros((num_tests, num_refs), dtype=int)


for test in range(num_tests):
    
    for ref in range(num_refs):
       
        scores = Scores[test, :, ref]
        
       
        winner_index = np.argmax(scores)
        
       
        winners[test, ref] = winner_index


print("Winners for Each Data Point:", winners)


candidate_names = [...]


winners_named = np.array([[candidate_names[winner] for winner in test_winners] for test_winners in winners])

print("Winners for Each Data Point (Named):")
for test in range(num_tests):
    for ref in range(num_refs):
        print(f"Test {test + 1}, Referee {ref + 1}: {winners_named[test][ref]}")
