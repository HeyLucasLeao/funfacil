import re
import pandas as pd

def cleaning_tweets(data, language='pt'):
    dataset = data.copy()
    dataset = dataset[dataset['language'] == language]
    dataset.drop_duplicates('tweet', inplace=True)
    dataset.drop_duplicates('username', inplace=True)
    dataset['hashtags'] = [", ".join(y for y in re.findall('\B#\w\w+', x)) for x in dataset['tweet']]
    dataset = dataset[['date','tweet','hashtags']]
    dataset.set_index('date', inplace=True)

    return dataset
