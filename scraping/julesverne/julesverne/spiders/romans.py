import scrapy


class RomansSpider(scrapy.Spider):
    name = 'romans'
    allowed_domains = ['abu.cnam.fr/']
    start_urls = ['http://abu.cnam.fr/cgi-bin/donner_html?ballon1/', 'http://abu.cnam.fr/cgi-bin/donner_html?begum2/', 'http://abu.cnam.fr/cgi-bin/donner_html?blocus3/', 'http://abu.cnam.fr/cgi-bin/donner_html?bounty1/', 'http://abu.cnam.fr/cgi-bin/donner_html?robur1/', 'http://abu.cnam.fr/cgi-bin/donner_html?tdm80j2/', 'http://abu.cnam.fr/cgi-bin/donner_html?tlun3/']

    def parse(self, response):
        pass
