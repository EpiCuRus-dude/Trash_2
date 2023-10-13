# Update the group_labels dictionary
group_labels = {
    1: [{'apple': '1'}, {'banana': '2'}, {'grapes': '4'}],
    2: [{'orange': '5'}, {'peach': '6'}, {'pear': '7'}, {'orange': '8'}]
}

# Re-flatten the group_labels for easier searching
flattened_group_labels = {group: {k: v for d in dicts for k, v in d.items()} for group, dicts in group_labels.items()}

# Initialize dictionaries for each group again
group_1_dict = {'true': [], 'pred': [], 'ids': []}
group_2_dict = {'true': [], 'pred': [], 'ids': []}

# Re-populate group dictionaries
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

# Add general IDs to the dictionaries
group_1_dict['general_ids'] = list(flattened_group_labels[1].values())
group_2_dict['general_ids'] = list(flattened_group_labels[2].values())

group_1_dict, group_2_dict
