def all_sublists(lst):
   
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))




from itertools import chain, combinations, product

def all_subsets(lst):
    
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))

def combine_lists(list_1, list_2):
    
    combs_list_1 = all_combinations(list_1)
    combs_list_2 = all_combinations(list_2)

   
    combined = [(comb1, comb2) for comb1, comb2 in product(combs_list_1, combs_list_2)]

    return combined


