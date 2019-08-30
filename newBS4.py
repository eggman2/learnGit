from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

# if has Chinese, apply decode()
# html = urlopen(
#     "https://morvanzhou.github.io/static/scraping/table.html"
# ).read().decode('utf-8')
# print(soup.h1)
# print('\n',soup.p)

# all_href = soup.find_all('p')
# all_href = [l['href'] for l in all_href]
# print(all_href)

# use class to narrow search
# month = soup.find_all('li',{'class':'month'})
# for m in month:
#     print(m.get_text())

# img_links = soup.find_all("img", {"src":re.compile('.*?\.jpg')})
# for link in img_links:
#     print(link['src'])

# course_link = soup.find_all("a",{'href':re.compile('https://morvan.*')})
# for link in course_link :
#     print(link['href'])

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank",
                                   "href": re.compile("/item/(%.{2})+$")})
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()

###TODO
"""getaddinfo failed
    逻辑：每次基于base url + his列表中最后一个元素来寻找所有a href标签，放到sub_urls列表
    若该列表长不为0，从中随机得到一个href标签，获得内容append到his列表，继续下一次循环
    如果长度为0，表示没有找到匹配的url，则弹出his列表中最后一个添加的元素，回退到上一次的url继续"""
