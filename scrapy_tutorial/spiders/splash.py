# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/page/2/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        for q in response.css("div.quote"):
            author = q.css(".author::text").extract_first()
            quote = q.css(".text::text").extract_first()
            # CHALLENGE get the tags for each quote using xpath.
            yield quote
        # CHALLENGE get the quotes from the first 4 pages.
