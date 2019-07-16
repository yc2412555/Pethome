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
    cat_vari_img = scrapy.Field()
    en_name = scrapy.Field()
    alias = scrapy.Field()
    weight = scrapy.Field()
    shape = scrapy.Field()
    origin = scrapy.Field()
    price = scrapy.Field()
    cat_habit = scrapy.Field()
    # cat_character = scrapy.Field()
    sti_degree = scrapy.Field()
    bar_degree = scrapy.Field()
    hair_loss_degree = scrapy.Field()
    fri_degree = scrapy.Field()
    ani_fri_degree = scrapy.Field()
    trainability = scrapy.Field()
    city_degree = scrapy.Field()
    feature = scrapy.Field()
    attention = scrapy.Field()
    nurturing_knowledge = scrapy.Field()

