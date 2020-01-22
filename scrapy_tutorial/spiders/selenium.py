# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import TextResponse
from time import sleep
import os
# IMPORTANT 
# selenium is a package for driving dynamic web pages using a virtual browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# in this project we are using Chrome as browser, so it is necessary for you to have 
# google chrome installed on your machine and download the chromedriver that matches
# with its version. Then substitute the path with the installation path
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
# IMPORTANT

class SeleniumSpider(scrapy.Spider):
    name = 'selenium'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions?tab=Votes']

    def __init__(self, *args, **kwargs):
        # Here, the selenium chromedriver is starting, this is executed as first of all in the spider logic.
        super(SeleniumSpider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        # CHALLENGE right now, this spider scrapes only the first result on the results list
        # the objective is to crawl all the results in the first three result pages
        # to achieve that, use selenium's click option to navigate to the next.
        # It would be great if the solution recicles the parse function.

        sleep(3)
        print('URL=', self.driver.current_url)

        self.driver.find_element_by_xpath('(//div[@id="questions"]/div/div[@class="summary"]/h3/a)[1]').click()
        sleep(3)

        print('URL=', self.driver.current_url)
        yield response.follow(self.driver.current_url, self.parse_content)

        links = response.xpath('//div[@id="questions"]/div/div[@class="summary"]/h3/a/@href').extract()
        pass

    def parse_content(self, response):
        title = response.xpath('//div[@id="question-header"]/h1/a/text()').extract_first()
        # CHALLENGE get the text from the question
        # CHALLENGE if there are, get the text from the first two comments
        # CHALLENGE if there are, get the text from the first two answers
        yield {
            'title': title
        }
