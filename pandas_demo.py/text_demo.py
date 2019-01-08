# -*- coding: UTF-8 -*-
import pandas as pd
from nltk.stem import PorterStemmer

train = pd.read_csv('./datas/twitter.csv')

from textblob import Word
train['tweet'] = train['tweet'].apply(lambda x: " ".join(
    [Word(word).lemmatize() for word in x.split()]))
train['tweet'].head()
print(train)





