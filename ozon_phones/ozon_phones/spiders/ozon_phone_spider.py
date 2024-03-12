from distutils.file_util import move_file
from typing import Iterable

import scrapy
from scrapy import Request
from scrapy.http import Response

from ozon_phones.html_selectors import card_href_selector, mobile_name_selector, system_version_selector
from ozon_phones.items import OzonPhonesItem
from ozon_phones.selenium_request import Scroll, SeleniumRequest


class OzonPhoneSpider(scrapy.Spider):
    name = "ozon-phone"
    category_uri = "/category/smartfony-15502/"
    domain = "https://www.ozon.ru"

    def start_requests(self) -> Iterable[Request]:
        for i in range(7, 10):
            page_url = self.domain + self.category_uri + f"?page={i}"
            yield SeleniumRequest(url=page_url, callback=self.parse_product_list, scroll=Scroll(length=5000))

    def parse_product_list(self, response: Response):
        for uri in card_href_selector(response):
            url = self.domain + uri
            yield SeleniumRequest(url, callback=self.parse_item, scroll=Scroll(length=5000))

    def parse_item(self, response: Response) -> OzonPhonesItem | None:
        version = system_version_selector(response)
        mobile_name = mobile_name_selector(response)
        if version and mobile_name:
            return OzonPhonesItem(name=mobile_name, os_version=version)
        return None
