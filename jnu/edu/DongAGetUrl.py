# -*- coding:utf-8 -*-
'''
Created on 2018. 3. 31.

@author: coco
'''


# 동아 전용 크롤러
from bs4 import BeautifulSoup
import requests

OutputFN = 'url_out_dongA.txt'
open_outputFile = open(OutputFN, 'w')

urls = list()
outputUrls = list()

for t in range(1, 10):
    
    urls = "http://news.donga.com/List?p=" + str((t * 20) - 19) + "&prod=news&ymd=&m="
    print(urls)
    response = requests.get(urls)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    for a in soup.find_all('a', href=True):
        if "http://news.donga.com/List/3/all/" in a['href']:
            #if not "http" in a['href']:
            outputUrls.append(a['href'])
                    
setOutputUrls = list(set(outputUrls))

for i in setOutputUrls:
    print(i)
    open_outputFile.write(i +"\n")
    
open_outputFile.close()