import json
from dataclasses import asdict

from scrapy import Spider

from .items import OzonPhonesItem


class OzonPhonesPipeline:
    def open_spider(self, spider):
        self.file = open("items.jsonl", "a", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item: OzonPhonesItem, spider: Spider):
        line = json.dumps(asdict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
