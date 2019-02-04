from scrapy import Spider
from scrapy.selector import HtmlXPathSelector
from imdb.items import IMDBItem, Field

class IMDBSpider(Spider):
    name = 'imdb'
    allowed_domains = ["imdb.com"]
    start_urls = [
        "https://www.imdb.com/chart/top"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//tbody[@class="lister-list"]/tr')
        items = []
        for site in sites:
            item = IMDBItem()
            item['title'] = site.select('td[@class="titleColumn"]/a/text()').extract()
            item['year'] = site.select('td[@class="titleColumn"]/span/text()').extract()
            item['rating'] = site.select('td[@class="ratingColumn imdbRating"]/strong/text()').extract()
            items.append(item)
        return items