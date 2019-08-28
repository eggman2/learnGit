from bs4 import BeautifulSoup
from urllib.request import urlopen

#if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/list.html"
).read().decode('utf-8')
# print(html)
soup = BeautifulSoup(html, features='lxml')
# print(soup.h1)
# print('\n',soup.p)

# all_href = soup.find_all('p')
# all_href = [l['href'] for l in all_href]
# print(all_href)

#use class to narrow search
# month = soup.find_all('li',{'class':'month'})
# for m in month:
#     print(m.get_text())

jan = soup.find_all('ul',{"class":"jan"},'li')
# d_jan = jan.find_all('li')
for d in jan:
    print(d.get_text())