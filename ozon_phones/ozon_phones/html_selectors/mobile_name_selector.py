def mobile_name_selector(response) -> str | None:
    return response.xpath('//div[@data-widget = "webProductHeading"]/h1/text()').get()
