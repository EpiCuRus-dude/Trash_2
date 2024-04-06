def all_sublists(lst):
   
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))




from itertools import chain, combinations, product

def all_subsets(lst):
    
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))

def combine_subsets(list_1, list_2):
    
    subsets_list_1 = all_subsets(list_1)
    subsets_list_2 = all_subsets(list_2)

    
    combined_subsets = list(product(subsets_list_1, subsets_list_2))

    return combined_subsets

