from bs4 import BeautifulSoup
import requests
from datetime import datetime

url='https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%8B%A4%EC%9D%8C+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

results=soup.findAll('strong','tit_rank')
search_rank_file=open('rankresult.txt','w')
rank=1

print(datetime.today().strftime('%Y년 %m월 %d일의 검색어 순위입니다.\n'))

for result in results:
    search_rank_file.write(str(rank)+"위 : "+result.get_text()+'\n')
    print(rank,"위: ",result.get_text(),'\n')
    rank+=1
