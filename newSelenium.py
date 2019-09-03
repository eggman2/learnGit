import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromewoptions = Options()
chromewoptions.add_argument('--headless')
broswer = webdriver.Chrome(options=chromewoptions,)
# executable_path='D:\Python3704\chromedriver.exe',

broswer.get("https://morvanzhou.github.io/")

broswer.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
time.sleep(2)
broswer.find_element_by_link_text("About").click()
time.sleep(2)

broswer.find_element_by_link_text(u"赞助").click()
time.sleep(2)

broswer.find_element_by_link_text(u"教程 ▾").click()
time.sleep(2)

broswer.find_element_by_link_text(u"数据处理 ▾").click()
time.sleep(2)

broswer.find_element_by_link_text(u"网页爬虫").click()

html = broswer.page_source
broswer.get_screenshot_as_file('./img/screenshot2.png')
broswer.close()
print(html[:200])