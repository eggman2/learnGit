import multiprocessing as mp
import time
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup
import re
base_url = "https://morvanzhou.github.io/"

def crawl(url):
    response = urlopen(url)
    return response.read().decode()

def parse(html):
    soup = BeautifulSoup(html,'lxml')
    urls = soup.find_all('a',{"href":re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url,url['href']) for url in urls])
    #去重

    url = soup.find('meta',{'property':'og:url'})['content']
    return title,page_urls,url

#--------------------------------------------single
#Don't OVER CRWAL THE WEBSITE OR YOU MAYNEVER VISIT AGAIN

if __name__ == '__main__':
    count ,t1= 1, time.time()
    pool = mp.Pool()
    restricted_crwal = False
    unseen = set([base_url,])
    seen=set()

    while(len(unseen)!=0):
        if restricted_crwal and len(seen)>=20:
            break

        print('\nDistributed Crawling...')
        crawling = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [cra.get() for cra in crawling ]

        print('\nDistributed Parsing...')
        parsing = [pool.apply_async(parse,args=(html,)) for html in htmls]
        results = [par.get() for par in parsing]

        print('\nAnalysing...')
        seen.update(unseen)
        unseen.clear()

        for title ,page_urls, url in results:
            print(count,title,url)
            count+=1
            unseen.update(page_urls - seen)
    print('total time: ^=%.1f s' % (time.time()-t1),)