# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UgirlsfileItem(scrapy.Item):
    image_urls = scrapy.Field()
    title=scrapy.Field()
    src=scrapy.Field()
    alt=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()

