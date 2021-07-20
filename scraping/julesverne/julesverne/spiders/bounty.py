import scrapy


class BountySpider(scrapy.Spider):
    name = 'bounty'
    allowed_domains = ['abu.cnam.fr/cgi-bin/donner_html?bounty1']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?bounty1/']

    def parse(self, response):
        pass
