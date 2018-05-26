# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HcmrealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    legal_status = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    num_of_floor = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    front_street_length = scrapy.Field()
    house_type = scrapy.Field() 
    project = scrapy.Field()
    district = scrapy.Field()
    url = scrapy.Field()
