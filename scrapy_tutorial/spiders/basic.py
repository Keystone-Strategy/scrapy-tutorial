# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["archive.org"]
    start_urls = (
        'http://www.archive.org/',
    )

    def parse(self, response):
        pass
