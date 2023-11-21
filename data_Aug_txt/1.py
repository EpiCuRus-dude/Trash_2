nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')



sample_data = {
    'A': ['The cat sleeps on the mat', 'A dog chased the ball', 'Fish swim in the ocean', 
          'Cats like to play with yarn', 'Dogs are great companions', 'A fish tank is calming',
          'The dog guards the house', 'Cats purr when happy', 'Fish can be colorful',
          'A playful dog', 'A lazy cat', 'Tropical fish are beautiful'],
    'B': ['cat', 'dog', 'fish', 'cat', 'dog', 'fish', 'dog', 'cat', 'fish', 'dog', 'cat', 'fish']
}


df_sample = pd.DataFrame(sample_data)







label_target_counts = {'cat': 1000, 'dog': 1000, 'fish': 1000}




duplication_df.head(), masking_df.head()

