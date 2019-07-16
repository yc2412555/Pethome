# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PethomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cat_vari_name = scrapy.Field()
    path = scrapy.Field()

