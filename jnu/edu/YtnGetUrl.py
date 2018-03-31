# -*- coding:utf-8 -*-
'''
Created on 2018. 3. 31.

@author: coco
'''


# ytn 전용 크롤러
from bs4 import BeautifulSoup
import requests

OutputFN = 'url_out_ytn.txt'
open_outputFile = open(OutputFN, 'w')

urls = list()
outputUrls = list()

for t in range(1, 10):
    
    urls = "http://www.ytn.co.kr/news/news_quick.php?page=" + str(t)
    print(urls)
    response = requests.get(urls)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #print(soup.find_all('dt'))
    
    # for p in soup.find_all('dt'):
    #     print("title : " + p.text)
    
    
    for a in soup.find_all('a', href=True):
        if "/_ln/" in a['href']:
            if not "http" in a['href']:
                outputUrls.append(a['href'])
                #print("Found the URL : " + a['href'])
                    
setOutputUrls = list(set(outputUrls))
# for x in outputUrls:
#     print("결과 : " + x);

for i in setOutputUrls:
    print("http://www.ytn.co.kr" + i)
    open_outputFile.write("http://www.ytn.co.kr" + i +"\n")
    
open_outputFile.close()