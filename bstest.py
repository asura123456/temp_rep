__author__ = 'Administrator'

from bs4 import BeautifulSoup

soup=BeautifulSoup(open('BeautifulSoup.html'),'lxml')
for i in soup.find_all('a',id="link2"):
    print(i)


print(soup.select('p .sister'))
print(soup.select('head>title'))
print(soup.select('a[id="link3"]'))