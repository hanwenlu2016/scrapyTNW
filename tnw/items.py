# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TnwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 昵称
    name = scrapy.Field()
    # 职业
    profession = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 籍贯
    place = scrapy.Field()
    # 个人主页
    home = scrapy.Field()
    # 宣言
    manifesto = scrapy.Field()