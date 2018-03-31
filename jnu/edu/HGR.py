# -*- coding:utf-8 -*-
'''
Created on 2018. 3. 31.

@author: coco
'''


# 한겨레 전용
from bs4 import BeautifulSoup
import requests

OutputFN = 'url_out_HGR.txt'
open_outputFile = open(OutputFN, 'w')

urls = list()
outputUrls = list()

for t in range(1, 10):
    
    urls = "http://www.hani.co.kr/arti/list" + str(t) + ".html"
    print(urls)
    response = requests.get(urls)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    for a in soup.find_all('a', href=True):
        if "/arti/" in a['href']:
            if not "http" in a['href']:
                if ".html" in a['href']:
                    if not "list" in a['href']:
                        if not "gallery" in a['href']:
                            outputUrls.append(a['href'])
                            print("Found the URL : " + a['href'])
                    
setOutputUrls = list(set(outputUrls))
print(setOutputUrls)

for i in setOutputUrls:
    print("http://www.hani.co.kr" + i)
    open_outputFile.write("http://www.hani.co.kr" + i +"\n")
    
open_outputFile.close()