'''
This file takes in the scraped news urls and generate a dictionary for that article.
article = {
    article-id : ....,
    category: ....,
    url: ...,
    title: ...,
    news_text: ...,
}
'''

import requests
from bs4 import BeautifulSoup
import pickle
import math
import time

file = open('/home/moksh/qure_setup/data_urls/url_2015', 'rb')
# dump information to that file
links = pickle.load(file)

cnt = 0
err_count=0
for urls in links:
    cnt+=1
    print("Count = " + str(cnt))
    try:
        URL = urls
        page = requests.get(URL)
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
        
        #news_collect.append(article)
        
        
    #news_day[day] = news_collect
        path = '/home/moksh/qure_setup/news_data/' + str(article['id']) + ".pkl"
        file = open(path, 'wb')

        pickle.dump(article, file)

        file.close()
        time.sleep(1)
    except:
        err_count+=1
        print("Error Count = " + str(err_count))
        
        

