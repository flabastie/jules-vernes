import scrapy


class RoburSpider(scrapy.Spider):
    name = 'robur'
    allowed_domains = ['abu.cnam.fr/cgi-bin/donner_html?robur1']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?robur1/']

    def parse(self, response):
        pass
