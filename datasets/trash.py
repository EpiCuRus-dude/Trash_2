from torchtext.datasets import ....
train_iter, test_iter = ...(split=('train', 'test'))

from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

tokenizer = get_tokenizer('basic_english')
def yield_tokens(data_iter):
    for label, text in data_iter:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])

text_pipeline = lambda x: [vocab[token] for token in tokenizer(x)]
label_pipeline = lambda x: int(x)

import csv



def save_to_csv(data_iter, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'text'])  # writing the headers
        for label, text in data_iter:
            writer.writerow([label, text])

train_iter, test_iter = ...(split=('train', 'test'))
save_to_csv(train_iter, '..._train.csv')
save_to_csv(test_iter, '..._test.csv')

import pandas as pd

def data_to_dataframe(data_iter):
    # Create a DataFrame directly from the iterator
    df = pd.DataFrame([(label, text) for label, text in data_iter], columns=['label', 'text'])
    return df

# Use the previously saved CSV or create a DataFrame directly
df_train = data_to_dataframe(train_iter)
df_train.to_csv('..._train_dataframe.csv', index=False)
df_test = data_to_dataframe(test_iter)
df_test.to_csv('..._test_dataframe.csv', index=False)



