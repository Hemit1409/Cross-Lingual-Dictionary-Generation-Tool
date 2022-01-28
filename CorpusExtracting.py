import requests
from bs4 import BeautifulSoup
import re
 
html = requests.get('https://www.divyabhaskar.co.in/local/gujarat/')
soup = BeautifulSoup(html.content,'html5lib')
# values = soup.find_all('p',{'style':'word-break:break-word'})
# print(values)
for val in soup.findAll('h3'):
    st=format(val.text)
    with open("Corpus_GUJ.txt","a",encoding="utf-8") as f:
       f.write(st+'\n')    