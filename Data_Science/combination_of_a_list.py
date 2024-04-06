def all_sublists(lst):
   
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))




from itertools import chain, combinations, product

def all_subsets(lst):
    
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))

def combine_subsets(list_1, list_2):
    subsets_list_1 = all_subsets(list_1)
    subsets_list_2 = all_subsets(list_2)

    combined_subsets = set()

    for subset1 in subsets_list_1:
        for subset2 in subsets_list_2:
            combined_subsets.add((frozenset(subset1), frozenset(subset2)))

    return [tuple(map(tuple, pair)) for pair in combined_subsets]

