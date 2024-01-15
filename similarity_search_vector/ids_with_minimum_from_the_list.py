# from different indeces
# what rows?


common_ids = set([item[0] for item in lists[0]])
for lst in lists[1:]:
    common_ids.intersection_update([item[0] for item in lst])
    if not common_ids:
        break  # Early termination if no common IDs

    
list_dicts = [{item[0]: item[1] for item in lst} for lst in lists]


id_value_sum = {id_: 0 for id_ in common_ids}
max_value = 0
for id_ in common_ids:
  for lst_dict in list_dicts:
      id_value_sum[id_] += lst_dict[id_]
  max_value = max(max_value, id_value_sum[id_])


max_ids = [id_ for id_, value in id_value_sum.items() if value == max_value]




