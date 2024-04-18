from torchtext.datasets import YahooAnswers
train_iter, test_iter = YahooAnswers(split=('train', 'test'))
