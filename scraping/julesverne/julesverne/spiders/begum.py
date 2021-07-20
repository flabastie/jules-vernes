import scrapy


class BegumSpider(scrapy.Spider):
    name = 'begum'
    allowed_domains = ['abu.cnam.fr/cgi-bin/donner_html?begum2']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?begum2/']

    def parse(self, response):
        pass
