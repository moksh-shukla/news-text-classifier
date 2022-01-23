'''
This file contains helper functions for the Flask application.
'''

import re
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

#function to scrape the news article
def scrape_article(url: str) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    info = soup.find('div', class_="articlepage")

    title_tag = info.find('h1', class_='title')
    title = title_tag.string
    title = title.split('\n')
    title = title[1]

    cat_tag = info.find('a', class_='section-name')
    cat = cat_tag.string
    cat = cat.split('\n')
    cat = cat[1]

    news_tagID = "content-body-14269002-" + str(info['data-artid']) 
    news_txt = soup.find('div', id = news_tagID)
    news_lst = news_txt.find_all('p')

    news = ''
    for txt in news_lst:
        news+=txt.text
        
    article = {}
    article['title'] = title
    #article['date_published'] = date
    article['id'] = info['data-artid']
    article['url'] = info['data-surl']
    article['category'] = cat
    article['news_text'] = news

    return article

# function to clean the text
def cleaning(text):
    news_txt = text
    news_txt = removeTag(news_txt)
    news_txt = removeSpec_char(news_txt)
    news_txt = lowerCase(news_txt)
    news_txt = remove_punc(news_txt)
    news_txt = lemmaWord(news_txt)
    news_txt = removeStop(news_txt)
    news_txt = lemmaWord(news_txt)

    return news_txt

## functions to clean the news text
def removeTag(text):
    remove = re.compile(r'')
    return re.sub(remove, '', text)

#removes special characters
def removeSpec_char(text):
    cleanString = text.replace("\n", " ")
    return cleanString

def lowerCase(text):
    return text.lower()

#removes punctuation
def remove_punc(text):
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    new_words = tokenizer.tokenize(text)
    return new_words

#removes stop words
def removeStop(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [x for x in words if x not in stop_words]

# lemmatizes the words
def lemmaWord(text):
    wordnet = WordNetLemmatizer()
    return " ".join([wordnet.lemmatize(word) for word in text])