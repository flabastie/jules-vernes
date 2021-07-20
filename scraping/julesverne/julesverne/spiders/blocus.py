import scrapy


class BlocusSpider(scrapy.Spider):
    name = 'blocus'
    allowed_domains = ['abu.cnam.fr/cgi-bin/donner_html?blocus3']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?blocus3/']

    def parse(self, response):
        pass
