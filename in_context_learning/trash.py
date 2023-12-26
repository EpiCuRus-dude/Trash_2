import pandas as pd


data = {'A': ['Question 1', 'Question 2'], 'B': ['Answer 1', 'Answer 2']}
df = pd.DataFrame(data)


messages = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    
    question_dict = {"role": "consumer", "question": row['A'] + "?"}
    
    answer_dict = {"role": "seller", "answer": "This is " + row['B'] + "?"}

   
    messages.extend([question_dict, answer_dict])


print(messages)
