from typing import Generator


def card_href_selector(response) -> Generator[str, None, None]:
    for i in response.css("a.tile-hover-target"):
        item_uri = i.xpath("@href").get()
        yield item_uri
