'''
This file is used to scrape all the news urls from archive page on a particular date and scrapes all such 
archive pages for the selected years
'''

import requests
from bs4 import BeautifulSoup
import time
import pickle

years = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
months = [i for i in range(1,13)]
odd_days = [i for i in range(1,32)]
even_days = [i for i in range(1,31)]
feb_leap = [i for i in range(1,30)]
feb_noleap = [i for i in range(1,29)]

data_dic = {}

for year in years:
    for month in months:
        print("Month = " + str(month))
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            days = odd_days
        elif month==2 and year%4!=0:
            days = feb_noleap
        elif month==2 and year%4==0:
            days = feb_leap
        else:
            days = even_days

        temp_day_dic = {}
        for day in days:
            print("Day = " + str(day))
            news_links = []
            URL = "https://www.thehindu.com/archive/web/"+ str(year)+ "/"+ str(month) +"/"+ str(day)+"/"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")

            #collects all categories on a particula archive page
            categ = soup.find(id="subnav-tpbar-latest")
            n = len(categ.findAll('a'))
            section_lst = []
            for i in range(1,n+1):
                section_lst.append('section_'+str(i))


            for section in section_lst:
                results = soup.find(id=section)
                section_elements = results.find("div", class_="col-lg-12 col-md-12 col-sm-12 col-xs-12")
                link_elements = section_elements.find('ul', class_= 'archive-list')

                for link in link_elements.findAll('li'):
                    news_links.append(link.a['href'])

            temp_day_dic[day] = news_links
            time.sleep(0.5)

        

        path = '/home/moksh/qure_setup/data/' + str(month)
        file = open(path, 'wb')

        # dump information to that file
        pickle.dump(temp_day_dic, file)

        # close the file
        file.close()
   
