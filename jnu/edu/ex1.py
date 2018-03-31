# -*- coding:utf-8 -*-
'''
Created on 2018. 3. 31.

@author: coco
'''

# import urllib.request
# from bs4 import BeautifulSoup
# import time
# 
# url = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100"
# response = urllib.request.urlopen(url)
# 
# soup = BeautifulSoup(response, "html.parser")
# results = soup.select("#selection_body .photo a")
# 
# for result in results:
#     print("제목: ", result.attrs["title"])
#     url_article = result.attrs["href"]
#     response = urllib.request.urlopen(url_article)
#     soup_article = BeautifulSoup(response, "html.parser")
#     content = soup_article.select_one("#articleBodyContents")
#     
#     output = ""
#     for item in content.contents:
#         stripped = str(item).strip()
#         if stripped == "" :
#             continue
#         if stripped[0] not in ["<", "/"]:
#             output =+ str(item).strip()
#     
#     output.replace("&apos;", "")
#     print(output.replace("기사 등", ""))
#     
#     time.sleep(5)

from bs4 import BeautifulSoup
import urllib.request
 
# 출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'
# 긁어 올 URL
URL = 'http://www.ytn.co.kr/_ln/0104_201803311548369872'

 
 
# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id="CmAdContent"):
        text = text + str(item.find_all(text=True))
    return text
 
 
# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()
    
 
if __name__ == '__main__':
    main()