import requests
from bs4 import BeautifulSoup
import os
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir2 = os.path.split(script_dir)[0]
print(script_dir2)
 
html = requests.get('https://www.divyabhaskar.co.in/local/gujarat/')
soup = BeautifulSoup(html.content,'html5lib')
# values = soup.find_all('p',{'style':'word-break:break-word'})
# print(values)
links=[]
for val in soup.findAll('li',{'class':"_24e83f49 e54ee612"}):
    links.append(val.a['href'])
    # print(links)
    
for link in links:
    page = requests.get('https://www.divyabhaskar.co.in/'+link)
    b = BeautifulSoup(page.content,'html5lib')
    for val in b.findAll('p',{'style':'word-break:break-word'}):
            st=format(val.text)
            with open(script_dir2+"\data\Corpus_GUJ2.txt","a",encoding="utf-8") as f:
                 f.write(st+'\n') 
