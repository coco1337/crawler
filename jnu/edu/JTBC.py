# -*- coding:utf-8 -*-
'''
Created on 2018. 3. 31.

@author: coco
'''


# JTBC 전용
from bs4 import BeautifulSoup
import requests

OutputFN = 'url_out_JTBC.txt'
open_outputFile = open(OutputFN, 'w')

urls = list()
outputUrls = list()

for t in range(1, 5):
    
    urls = "http://news.jtbc.joins.com/section/list.aspx?pdate=20180331&scode=&copyright=&pgi=" + str(t)
    print(urls)
    response = requests.get(urls)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    for a in soup.find_all('a', href=True):
        if "/article/article.aspx?news_id=" in a['href']:
            #if not "http" in a['href']:
            outputUrls.append(a['href'])
                    
setOutputUrls = list(set(outputUrls))

for i in setOutputUrls:
    print("http://news.jtbc.joins.com" + i)
    open_outputFile.write("http://news.jtbc.joins.com" + i +"\n")
    
open_outputFile.close()