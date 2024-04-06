def all_sublists(lst):
   
    return list(chain(*[combinations(lst, i) for i in range(1, len(lst) + 1)]))
