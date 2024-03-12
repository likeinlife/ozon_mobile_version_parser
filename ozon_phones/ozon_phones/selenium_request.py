from dataclasses import dataclass
from typing import Any, Callable

from scrapy import Request
from scrapy.responsetypes import Response


@dataclass(match_args=True)
class Scroll:
    wait_time: float = 2
    length: int = 5000


class SeleniumRequest(Request):
    def __init__(
        self,
        url: str,
        callback: Callable[[Response], Any],
        scroll: Scroll | None = None,
        *args,
        **kwargs,
    ):
        self.scroll = scroll

        super().__init__(*args, url=url, callback=callback, **kwargs)
