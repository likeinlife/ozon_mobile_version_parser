import time

import undetected_chromedriver as uc
from scrapy import signals
from scrapy.crawler import Crawler, Spider
from scrapy.http import HtmlResponse, Request, Response
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ozon_phones.errors import IncorrectRequestType
from ozon_phones.selenium_request import Scroll, SeleniumRequest


class SeleniumMiddleware:
    def __init__(self, headless: bool = False):
        options = uc.ChromeOptions()
        if headless:
            options.add_argument("--headless")

        self.driver = uc.Chrome(options=options)

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        headless = crawler.settings.get("HEADLESS", False)
        middleware = cls(headless)

        crawler.signals.connect(middleware.close, signals.spider_closed)

        return middleware

    def process_request(self, request: SeleniumRequest, spider: Spider):
        if not isinstance(request, SeleniumRequest):
            raise IncorrectRequestType(request)
        self.driver.get(request.url)

        WebDriverWait(self.driver, 15).until_not(EC.title_is("Antibot Challenge Page"))

        match request.scroll:
            case Scroll(wait_time, length):
                time.sleep(wait_time)
                self.driver.execute_script(f"window.scrollTo(5, {length});")
                time.sleep(wait_time)

        content = self.driver.page_source

        return HtmlResponse(request.url, encoding="utf-8", body=content, request=request)

    def process_response(self, request: Request, response: Response, spider: Spider):
        return response

    def _close(self):
        self.driver.close()
