from flask import Flask, send_file, request
import os
from itsdangerous import exc
import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
import pickle
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from helper import *

app = Flask(__name__, static_url_path='')

##### STUB FUNCTION FOR CLASS PREDICTION #####
labels = {'Economy': 0,
        'Entertainment': 1,
        'Industry': 2,
        'International': 3,
        'Lifestyle': 4,
        'Metrocity News': 5,
        'National': 6,
        'Opinion & Miscellaneous': 7,
        'Other States': 8,
        'Politics': 9,
        'Sci & Tech': 10,
        'South Regional': 11,
        'Sports': 12
        }
    

def get_key(val):
    for key, value in labels.items():
         if val == value:
             return key
             
#function to predict and return the class of the article
def predict_class(url: str) -> str:
    '''Predict the class of the news article at given URL'''
    news = scrape_article(url)
    news_txt = cleaning(news['news_text'])

    filename = 'files/modelRF.sav'
    model = pickle.load(open(filename, 'rb'))

    CV = CountVectorizer(max_features = 5000)

    df = pd.read_csv('files/data.csv')
    CV.fit_transform(df.news).toarray()
    news_bag = CV.transform([news_txt])
    ypred = model.predict(news_bag)
    class_name = get_key(ypred[0])

    return class_name

# GET route for class prediction
@app.route("/predict")
def predict():
    url = request.args.get("url")
    if url is None:
        return "Invalid URL"
    try:
        return predict_class(url)
    except:
        return "error"

# Render main page on GET /
@app.route("/")
def home_page():
    return send_file("static/index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
