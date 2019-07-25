
import pandas as pd
import numpy as np

#internet package

import urllib3
from bs4 import BeautifulSoup  
http = urllib3.PoolManager()

#functional package
import logging
import requests
from newspaper import Article
from newspaper import fulltext
from tqdm import tqdm
from tqdm import tnrange, tqdm_notebook

logging.basicConfig(filename="crawlfulltext.log",level=logging.ERROR)

def get_details_from_url(df_to_get):
    data_dicts = []
    for url in tqdm(df_to_get['url'].values):
        row_dict = {}
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            row_dict['url'] = url
            row_dict['fulltext'] = article.text
            row_dict['summary'] = article.summary
            row_dict['keywords'] = article.keywords
            data_dicts.append(row_dict)
        except Exception as e:
#             logging.error()
            continue
    return data_dicts

for item in tqdm(["aapl.csv","amzn.csv","fb.csv","googl,csv","msft.csv"]):
    news_url = pd.read_csv(item, usecols = range(0,2), encoding='latin-1')
    filename = item.split(".")[1]
    pd.DataFrame(get_details_from_url(news_url)).to_csv(filename + 'news.csv')






