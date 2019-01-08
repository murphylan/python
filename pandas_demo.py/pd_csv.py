# -*- coding: UTF-8 -*-

import pandas as pd

train = pd.read_csv('./datas/twitter.csv')
# print(train);

# train['word_count'] = train['tweet'].apply(lambda x: len(str(x).split(" ")))
# train[['tweet','word_count']].head()
# print(train);

# train['char_count'] = train['tweet'].str.len() ## 也包括空格
# train[['tweet','char_count']].head()
# print(train);


# def avg_word(sentence):
#     words = sentence.split()
#     return (sum(len(word) for word in words)/len(words))


# train['avg_word'] = train['tweet'].apply(lambda x: avg_word(x))
# train[['tweet', 'avg_word']].head()
# print(train)

# from nltk.corpus import stopwords
# stop = stopwords.words('english')

# train['stopwords'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x in stop]))
# train[['tweet','stopwords']].head()
# print(train)


# train['hastags'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
# train[['tweet','hastags']].head()
# print(train)


# train['numerics'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
# train[['tweet','numerics']].head()
# print(train)


train['upper'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x.isupper()]))
train[['tweet','upper']].head()
print(train)


