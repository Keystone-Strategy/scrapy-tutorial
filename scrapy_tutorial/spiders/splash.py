# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions?tab=Votes/']

    def parse(self, response):
        
        pass
