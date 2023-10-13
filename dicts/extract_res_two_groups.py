# Initialize dictionaries for each group
group_1_dict = {'true': [], 'pred': [], 'ids': []}
group_2_dict = {'true': [], 'pred': [], 'ids': []}

# The new A dictionary
A = {
    'true': ['apple', 'apple', 'banana', 'grapes', 'orange', 'peach', 'pear', 'orange'],
    'pred': ['banana', 'apple', 'apple', 'grapes', 'peach', 'orange', 'pear', 'orange']
}

# Flatten the group_labels for easier searching
flattened_group_labels = {group: {k: v for d in dicts for k, v in d.items()} for group, dicts in group_labels.items()}

# Helper function to identify the group and ID of a label
def identify_group_and_id(label):
    for group, labels in flattened_group_labels.items():
        if label in labels:
            return group, labels[label]
    return None, None

# Populate group dictionaries
for i in range(len(A['true'])):
    true_label, pred_label = A['true'][i], A['pred'][i]
    
    # For true label
    group, label_id = identify_group_and_id(true_label)
    if group == 1:
        group_1_dict['true'].append(true_label)
        group_1_dict['ids'].append(label_id)
    elif group == 2:
        group_2_dict['true'].append(true_label)
        group_2_dict['ids'].append(label_id)
        
    # For pred label
    group, label_id = identify_group_and_id(pred_label)
    if group == 1:
        group_1_dict['pred'].append(pred_label)
    elif group == 2:
        group_2_dict['pred'].append(pred_label)

group_1_dict, group_2_dict
