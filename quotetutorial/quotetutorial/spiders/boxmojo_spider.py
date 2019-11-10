import scrapy
from ..items import QuotetutorialItem

class BoxMojoSpider(scrapy.Spider):
    name = 'boxmojo'
    p = 2
    start_urls = [
        'https://www.boxofficemojo.com/title/tt0172156/?ref_=bo_rl_ti'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        abc = response.css(".a-size-extra-large::text").extract()
        bac = response.css(".mojo-hidden-from-mobile .a-spacing-none:nth-child(1) span:nth-child(1)::text ,.a-spacing-none:nth-child(1) span+ span::text").extract()
        efg =response.css(".mojo-hidden-from-mobile .a-spacing-none:nth-child(2) > span:nth-child(1)::text,.mojo-hidden-from-mobile .a-spacing-none:nth-child(2) .money::text").extract()
        pab =response.css(".mojo-hidden-from-mobile .a-spacing-none:nth-child(3) > span:nth-child(1)::text,.mojo-hidden-from-mobile .a-spacing-none~ .a-spacing-none+ .a-spacing-none .money::text").extract()
        qbd = response.css(".mojo-hidden-from-mobile .a-spacing-none:nth-child(4) span:nth-child(1)::text,.mojo-hidden-from-mobile .a-spacing-none:nth-child(4) span+ span::text").extract()
        rfd = response.css(".mojo-hidden-from-mobile .a-spacing-none:nth-child(6) span:nth-child(1)::text,.a-spacing-none:nth-child(6) span+ span::text").extract()
        sar = response.css(".mojo-hidden-from-mobile .a-spacing-none:nth-child(7) span:nth-child(1)::text,.a-spacing-none:nth-child(7) span+ span::text").extract()
        sar0 = response.css(".a-align-center .a-link-normal::text,.a-align-center:nth-child(2)::text").extract()
        sar00 = response.css("th:nth-child(3)::text,.a-align-center:nth-child(3)::text").extract()
        sar1 = response.css("th:nth-child(4)::text,.a-align-center:nth-child(4) .money::text").extract()
        sar2 = response.css("th:nth-child(5)::text,.a-align-center:nth-child(5) .money::text").extract()
        sar3 = response.css(".a-text-right~ .a-text-right+ .a-text-right::text,.a-text-right~ .a-align-center+ .a-align-center .money::text").extract()
        items['abc'] = abc
        items['bac'] =bac
        items['efg']=efg
        items['pab']=pab
        items['qbd']=qbd
        items['rfd']=rfd
        items['sar']=sar
        items['sar0']=sar0
        items['sar1']=sar1
        items['sar2'] = sar2
        items['sar3'] = sar3
        items['sar00'] = sar00
        yield items


