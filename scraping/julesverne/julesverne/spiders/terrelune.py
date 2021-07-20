import scrapy


class TerreluneSpider(scrapy.Spider):
    name = 'terrelune'
    allowed_domains = ['abu.cnam.fr/cgi-bin/donner_html?tlun3']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?tlun3/']

    def parse(self, response):
        pass
