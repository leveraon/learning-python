# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlingItem(scrapy.Item):
    tariff_item = scrapy.Field()
    harmonized_system_header = scrapy.Field()
    idicative_description = scrapy.Field()
    pass
