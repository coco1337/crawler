# -*- coding:utf-8 -*-
'''
Created on 2018. 3. 31.

@author: coco
'''

from bs4 import BeautifulSoup
import requests

OUTPUT_FN = 'output1.txt'
URL = "http://www.ytn.co.kr/_ln/0104_201803311548369872"
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.find(id='CmAdContent').text)

open_opfile = open(OUTPUT_FN, 'w')
open_opfile.write(soup.find(id='CmAdContent').text)
open_opfile.close()
