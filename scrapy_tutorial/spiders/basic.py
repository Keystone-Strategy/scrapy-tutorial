# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["archive.org"]
    start_urls = (
        'http://www.archive.org/',
    )

    def parse(self, response):
        # To navigate to the desired pages, here we are getting the links to those pages, as a list of strings
        links = response.xpath('//ul[@id="nav-abouts"]/li/a/@href').extract() 

        for link in links:
            if not link.startswith('https:'):
                continue
            yield response.follow(link, self.parse_content)

    def parse_content(self, response):
        text_list = response.xpath('//div[@class="col-md-9"]/p/text()').extract()
        # CHALLENGE: get the samne text_list but using .css selector instead of xpath.
        title = response.xpath('').extract_first()
        # CHALLENGE: get the title on the pages where you can using the xpath selector.

        text = ''
        for text_shard in text_list:
            text = text + text_shard

        # As this is the last yield, from here, the data goes to pipelines, to be processed
        yield {
            'text': text,
            'title': title
        }