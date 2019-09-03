import scrapy
import time
class BaoSpider(scrapy.Spider):
    name = 'Bao'
    start_urls = [
        'https://morvanzhou.github.io/',
    ]

    def parse(self,response):
        t1 = time.time()

        yield{
            'title':response.css('h1::text').extract_first(default='Missing').strip().replace('"',""),
            'url':response.url,
        }


        urls = response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            yield response.follow(url,callback=self.parse)
        print(time.time()-t1)