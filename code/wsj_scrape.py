#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:17:17 2020

@author: xiaoming
"""
import requests
from bs4 import BeautifulSoup
import bs4
import time
import random

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': '} # you should put your own cookies
url = "https://www.wsj.com/search/term.html?KEYWORDS=？&page=" # you should put your own keywoeds in ? and pages after =
proxies = [] # youshould put your proxies here

link=[]
for i in range(1,80):
    r = requests.get(url+str(i),cookies = cookies, headers = headers,proxies=random.choice(proxies),timeout = 30,allow_redirects=True)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,"html5lib")
    link1=soup.find_all('h3',{'class':"headline"})
    for s in link1:
        if "articles" in s.a['href']:
            link.append('https://www.wsj.com' + s.a['href'])
link=list(set(link))
link

f = open('','w',encoding='utf8') #put your path here
e=0
for q in link:
    try:
        article=requests.get(q,cookies = cookies, headers = headers, proxies=random.choice(proxies),timeout = 30)
    except:
        pass        
    soup=BeautifulSoup(article.text,'html.parser')
    abc=soup.find_all('p',{'class':[]})
    print(e)
    e=e+1
    for i in abc[1:-2]:  
        if ('class' and 'http') not in i:
            f.write(str(i.text))
            f.write("\n")    
    time.sleep(0.3)
f.close()
