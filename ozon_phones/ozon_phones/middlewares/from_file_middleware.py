from scrapy.crawler import Spider
from scrapy.http import HtmlResponse, Request, Response


class FromFileMiddleware:
    def process_request(self, request: Request, spider: Spider):
        with open("test.html", "r", encoding="utf-8") as file_obj:
            content = file_obj.read()

        return HtmlResponse(
            request.url, encoding="utf-8", body=content, request=request
        )

    def process_response(self, request: Request, response: Response, spider: Spider):
        return response
