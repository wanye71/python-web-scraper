import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
       return {
           "schema": response.xpath('//link[@rel="schema.DC"]/@href').get(),
           "author": response.xpath('//span[@class="author-name"]/text()').get(),
           "rfc-number": response.xpath('//span[@class="rfc-no"]/text()').get(),
           "author-co": response.xpath('//span[@class="author-company"]/text()').get(),
           "date": response.xpath('//span[@class="date"]/text()').get(),
           "title": response.xpath('//span[@class="title"]/text()').get(),
           "address": response.xpath('//span[@class="address"]/text()').get(),
           "headings": response.xpath('//span[@class="subheading"]/text()').get(),
       }
