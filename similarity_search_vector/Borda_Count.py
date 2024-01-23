def borda_count(rankings):

    scores = {}
    for rank in rankings:
        for i, item in enumerate(rank):
            scores[item] = scores.get(item, 0) + (len(rank) - i)


    aggregated_ranking = sorted(scores, key=scores.get, reverse=True)
    return aggregated_ranking


rank1 = [5, 3, 2, 4]  
rank2 = [2, 3, 5, 1]  

aggregated_rank = borda_count([rank1, rank2])
print("Aggregated Ranking:", aggregated_rank)
