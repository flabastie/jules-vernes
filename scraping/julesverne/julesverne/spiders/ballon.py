import scrapy


class BallonSpider(scrapy.Spider):
    name = 'ballon'
    allowed_domains = ['abu.cnam.fr/']
    start_urls = ['https://abu.cnam.fr/cgi-bin/donner_unformated?ballon1/']

    def parse(self, response):
        body = response.xpath("//body").get()

        yield {
            'body' : body
        }