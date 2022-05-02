#!/usr/bin/env python
# coding: utf-8

# #### 1)Write a python program to display all the header tags from wikipedia.org.

# In[1]:


import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


# In[2]:


html = urlopen('https://en.wikipedia.org/wiki/Main_Page')


# In[3]:


bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# #### 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)and make data frame.

# In[4]:


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


# In[5]:


movie_name = soup.select('td.titleColumn')
rating = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]


# In[6]:


list = []


# In[7]:


for index in range(0,101):
    movie_string = movie_name[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"name": movie_title,
            "rating": rating[index],
           "year_of_release": year,}
    list.append(data)


# In[8]:


movie_data=pd.DataFrame(list)
movie_data


# #### 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[9]:


url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


# In[10]:


movie_name = soup.select('td.titleColumn')
rating = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]


# In[11]:


list_ind=[]
for index in range(0,101):
    movie_string = movie_name[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"name": movie_title,
            "rating": rating[index],
           "year_of_release": year,}
    list_ind.append(data)


# In[12]:


movie_data=pd.DataFrame(list_ind)
movie_data


# #### 4 ) Write a python program to scrape product name, price and discounts from https://meesho.com/bags-ladies/pl/p7vbp 

# In[13]:


url="https://meesho.com/bags-ladies/pl/p7vbp"
html = urlopen(url)
soup = BeautifulSoup(html.read(),"html.parser") 


# In[14]:


print(soup.prettify())


# In[15]:


results=soup.find_all('div',{'class':"Card__BaseCard-sc-b3n78k-0 fa-dWHP NewProductCard__CardStyled-sc-j0e7tu-0 fqpiyA NewProductCard__CardStyled-sc-j0e7tu-0 fqpiyA"})


# In[16]:


len(results)


# In[17]:


results[0].find('p',{'class':"Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"}).get_text()


# In[18]:


results[0].find('h5',{'class':"Text__StyledText-sc-oo0kvp-0 hiHdyy"}).get_text()


# In[19]:


results[0].find('span',{'class':"Text__StyledText-sc-oo0kvp-0 lnonyH"}).get_text()


# In[20]:


prod_name=[]
price=[]
disc_avail=[]

for i in results:
    prod_name.append(i.find('p',{'class':"Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"}).get_text())
    price.append(i.find('h5',{'class':"Text__StyledText-sc-oo0kvp-0 hiHdyy"}).get_text())
    disc_avail.append(i.find('span',{'class':"Text__StyledText-sc-oo0kvp-0 lnonyH"}).get_text())


# In[21]:


data=pd.DataFrame({'product':prod_name,"price":price,"discount_offered":disc_avail})
data


# #### 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# #### a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating

# In[22]:



   url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
html = urlopen(url)
soup = BeautifulSoup(html.read(),"html.parser") 


# In[23]:


print(soup.prettify())


# In[24]:


results=soup.find_all('tr',{'class':"table-body"})
result=soup.find_all('tr',{'class':"rankings-block__banner"})
results=result+results


# In[25]:


len(results)


# In[26]:


results[0].find('span',{'class':"u-hide-phablet"}).get_text()#team


# In[27]:


results[0].find('td',{'class':"rankings-block__banner--matches"}).get_text()#1strankmatch


# In[28]:


results[1].find('td',{'class':"table-body__cell u-center-text"}).get_text()#othermatch


# In[29]:


results[0].find('td',{'class':"rankings-block__banner--points"}).get_text()#1strankpoints


# In[30]:


results[1].find('td',{'class':"table-body__cell u-center-text"}).get_text()#otherpoints


# In[2]:


first_data=soup.find("div",attrs={"rankings-block__container full rankings-table"}).find("div",class_="rankings-block__top-player").get_text(strip=True,separator=" ").split(" ")

other_data=soup.find("div",attrs={"rankings-block__container full rankings-table"}).find_all("tr",class_="table-body")

final_lst=[]
final_lst.append(first_data)

for i in data:
    split_lst=i.get_text(strip=True,separator=" ").split(" ")
    final_lst.append(split_lst)


# In[ ]:




