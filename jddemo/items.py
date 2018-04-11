# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JddemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    bookName = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    BookID = scrapy.Field()
    press = scrapy.Field()
    PreferentialPrice = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
