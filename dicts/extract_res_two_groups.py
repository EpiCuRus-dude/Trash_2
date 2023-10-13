group_labels = {
    1: [{'apple': '1', 'banana': '2'}, {'apple': '3', 'grapes': '4'}],
    2: [{'orange': '5', 'peach': '6'}, {'pear': '7', 'orange': '8'}]
}

A = {
    'true': {
        1: ['apple', 'apple', 'banana', 'grapes'],
        2: ['orange', 'peach', 'pear', 'orange']
    },
    'pred': {
        1: ['banana', 'apple', 'apple', 'grapes'],
        2: ['peach', 'orange', 'pear', 'orange']
    }
}
from collections import defaultdict

# Example dictionaries
group_labels = {
    1: [{'apple': '1', 'banana': '2'}, {'apple': '3', 'grapes': '4'}],
    2: [{'orange': '5', 'peach': '6'}, {'pear': '7', 'orange': '8'}]
}

A = {
    'true': {
        1: ['apple', 'apple', 'banana', 'grapes'],
        2: ['orange', 'peach', 'pear', 'orange']
    },
    'pred': {
        1: ['banana', 'apple', 'apple', 'grapes'],
        2: ['peach', 'orange', 'pear', 'orange']
    }
}

# Initialize the dictionaries for each group
group_1_dict = defaultdict(list)
group_2_dict = defaultdict(list)

# Helper function to fill the dictionary for each group
def fill_group_dict(group_dict, group_number):
    for label_type in ['true', 'pred']:
        group_dict[label_type] = A[label_type][group_number]
    
    group_dict['ids'] = []
    for label in A['true'][group_number]:
        for label_dict in group_labels[group_number]:
            if label in label_dict:
                group_dict['ids'].append(label_dict[label])

# Fill the dictionaries
fill_group_dict(group_1_dict, 1)
fill_group_dict(group_2_dict, 2)

group_1_dict, group_2_dict


