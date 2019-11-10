import scrapy
from scrapy.http.request import Request
from scrapy.spiders import CrawlSpider,Rule
from ..items import QuotetutorialItem
from scrapy.linkextractors import LinkExtractor
from lxml import html

class mySpider(CrawlSpider):
    name = "education3"
    allowed_domains = ["data.un.org"]
    start_urls = (
        'http://data.un.org/Data.aspx?d=UNESCO&f=series%3ANER_1',
        )

    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="linkNextB"]',)), callback="parse", follow= True),)

    def parse(self,response):
        for tr in response.xpath('//*[@id="divData"]/div/table/tr'):
            item =  QuotetutorialItem()
            item['country'] = tr.xpath('./td[1]/text()').extract_first()
            item['years'] = tr.xpath('./td[position()>1]/text()').extract()
            print(item)
            yield item