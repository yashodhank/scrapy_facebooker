# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FacebookPost(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    page_title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    shares_number = scrapy.Field()