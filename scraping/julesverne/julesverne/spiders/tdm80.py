import scrapy


class Tdm80Spider(scrapy.Spider):
    name = 'tdm80'
    allowed_domains = ['abu.cnam.fr/cgi-bin/donner_html?tdm80j2']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?tdm80j2/']

    def parse(self, response):
        pass
