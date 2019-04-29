# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnameItem(scrapy.Item):
    # define the fields for your item here like:
    ename = scrapy.Field()
    pronunciation = scrapy.Field()
    cname = scrapy.Field()
    cname_ext = scrapy.Field()
    gender = scrapy.Field()
    origin = scrapy.Field()
    moral = scrapy.Field()
    meaning = scrapy.Field()
    impression = scrapy.Field()
    similar = scrapy.Field()
