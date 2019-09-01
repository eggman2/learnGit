import requests
import webbrowser
# param = {"wd":"莫烦python"}
# r = requests.get('http://www.baidu.com/s',params=param)
# print(r.url)
# webbrowser.open(r.url)

# data = {'firstname':'莫烦','lastname':'周'}
# file =  {'uploadFile':open('./image.png','rb')}
# r = requests.post('http://pythonscraping.com/pages/files/processing2.php',
#                   # data=data)
#                   files=file)


# session = requests.Session()
# payload = {'username': 'Morvan', 'password': 'password'}
# r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
#
# # {'username': 'Morvan', 'loggedin': '1'}
#
#
# r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
# print(r.text)


# TODO
# 下载网页
# import os
# os.makedirs('./img/',exist_ok=True)
#
# IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
#
# from urllib.request import  urlretrieve
# urlretrieve(IMAGE_URL, './img/image1.png')

# 用urlretrieve下载


# import requests
# r= requests.get(IMAGE_URL)
# with open('./img/image2.png','wb') as f:
#     f.write(r.content)
# #用get下载，再用with存储


from bs4 import BeautifulSoup
import requests
import re

URL = "http://wallpaperswide.com/"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_url = soup.find_all('img', {'src': re.compile('http.*\.jpg$')})
print(img_url)
for l in img_url:
    url = l['src']
    r = requests.get(url, stream=True)
    print(url)
    image_name = url.split('/')[-1]
    print(image_name)
    # with open('./img/%s' % image_name, 'wb') as f:
    #     for chunk in r.iter_content(chunk_size=128):
    #         f.write(chunk)
    #     print('Save %s' % image_name)
# print(img_url)
