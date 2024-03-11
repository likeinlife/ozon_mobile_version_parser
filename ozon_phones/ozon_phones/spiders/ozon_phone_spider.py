from typing import Iterable

import scrapy
from scrapy import Request
from scrapy.http import Response

from ozon_phones.custom_request import Scroll, SeleniumRequest
from ozon_phones.html_selectors import android_version_selector, card_href_selector


class OzonPhoneSpider(scrapy.Spider):
    name = "ozon-phone"
    domain = "https://www.ozon.ru"

    def start_requests(self) -> Iterable[Request]:
        page_url = "https://www.ozon.ru/category/smartfony-15502/"
        page_url = "https://www.ozon.ru/product/realme-smartfon-note-50-4-128-gb-chernyy-1388203331/"
        # page_url = 'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?page=2'
        # page_url = "https://quotes.toscrape.com/"
        # yield SeleniumRequest(
        #     url=page_url, callback=self.parse_product_list, scroll=Scroll()
        # )
        yield SeleniumRequest(
            page_url, callback=self.parse_item, scroll=Scroll(length=1500)
        )

    def parse_product_list(self, response: Response):
        for uri in card_href_selector(response):
            url = self.domain + uri
            yield SeleniumRequest(
                url, callback=self.parse_item, scroll=Scroll(length=1500)
            )

    def parse_item(self, response: Response) -> None:
        android_version = android_version_selector(response)
        if android_version:
            print(android_version)
