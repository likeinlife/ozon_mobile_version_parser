BOT_NAME = "ozon_phones"

SPIDER_MODULES = ["ozon_phones.spiders"]
NEWSPIDER_MODULE = "ozon_phones.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

HEADLESS = False


# SPIDER_MIDDLEWARES = {
#    "ozon_phones.middlewares.OzonPhonesSpiderMiddleware": 543,
# }

DOWNLOADER_MIDDLEWARES = {
    "ozon_phones.middlewares.SeleniumMiddleware": 543,
    # "ozon_phones.middlewares.FromFileMiddleware": 543,
}

ITEM_PIPELINES = {
    "ozon_phones.pipelines.OzonPhonesPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
