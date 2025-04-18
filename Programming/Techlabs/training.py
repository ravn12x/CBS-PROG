import torch
import pandas as pd
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification

df = pd.read_csv('https://gist.githubusercontent.com/Mukilan-Krishnakumar/e998ecf27d11b84fe6225db11c239bc6/raw/74dbac2b992235e555df9a0a4e4d7271680e7e45/imdb_movie_reviews.csv')
df = df.drop('sentiment',axis=1)


tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')


def sentiment_movie_score(movie_review):
	token = tokenizer.encode(movie_review, return_tensors = 'pt')
	result = model(token)
	return int(torch.argmax(result.logits))+1


df['sentiment'] = df['text'].apply(lambda x: sentiment_movie_score(x[:512]))


df.head()

import wandb
wandb.init(project="BERT_Sentiment_Analysis")
wandb.run.log({"Sentiment Analysis of IMDB Movie Reviews" : wandb.Table(dataframe=df)})
wandb.run.finish()