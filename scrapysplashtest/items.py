# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class PyBooksItem(scrapy.Item):
    name=scrapy.Field()
    comment=scrapy.Field()
    promo_words=scrapy.Field()