# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tnw.items import TnwItem
from scrapy_redis.spiders import RedisSpider,RedisCrawlSpider


class TnSpider(RedisCrawlSpider):
    name = 'tn'
    # allowed_domains = ['http://www.taonanw.com']
    # start_urls = ['http://http://www.taonanw.com/']

    # 第一级匹配规则每一页链接匹配规则
    redis_key = "tn_urls"
    page = LinkExtractor(
        allow=r'http://www.taonanw.com/page/search_result_v2/p/\d+/search_type/search_quick/page_key/93e0a62a085397e93da5ed4bb727e0be/match_gender/1/match_r_city_id/440300/match_age_min/22/match_age_max/26/items_file/search_result_v2/total/2000/match_r_state_id/1339/n/20/list_style/2')

    # 第二级匹配规则：每个女性个人主页的匹配规则
    links = LinkExtractor(allow=r'http://www.taonanw.com/u_\d+')

    rules = (
        Rule(page),
        Rule(links, callback='parse_item'),)

    def parse_item(self, response):
        y = TnwItem()
        # 昵称
        y['name'] = self.get_name(response)

        # 职业
        y['profession'] = self.get_profession(response)

        # 年龄
        y['age'] = self.get_age(response)

        # 学历
        y['education'] = self.get_education(response)

        # 籍贯
        y['place'] = self.get_place(response)

        # 个人主页
        y['home'] = response.url

        # 宣言
        y['manifesto'] = self.get_manifesto(response)

        yield y

    # 获取昵称函数
    def get_name(self, response):
        names = response.xpath('//div[@class="fl"]/a/h1/text()').extract()

        if len(names):
            names = names[0]
        else:
            names = 'NULL'
        return names.strip()

    # 获取职业函数
    def get_profession(self, response):
        professions = response.xpath('//div[@id="baseinfo"]//span[@id="profile_occupation"]/a/text()').extract()

        if len(professions):
            professions = professions[0]
        else:
            professions = '保密'
        return professions.strip()

    # 获取年龄函数
    def get_age(self, response):
        ages = response.xpath('//div[@id="baseinfo"]//span[@id="profile_age"]/text()').extract()

        if len(ages):
            ages = ages[0]
        else:
            ages = 'NULL'
        return ages.strip()

    # 获取学历函数
    def get_education(self, response):
        educations = response.xpath('//div[@id="baseinfo"]//span[@id="profile_education"]/text()').extract()

        if len(educations):
            educations = educations[0]
        else:
            educations = 'NULL'
        return educations.strip()

    # 获取籍贯函数
    def get_place(self, response):
        places = response.xpath('//span[@id="profile_n_state_id"]/text()').extract()

        if len(places):
            places = places[0]
        else:
            places = 'NULL'
        return places.strip()

    # 获取宣言函数
    def get_manifesto(self, response):
        manifestos = response.xpath('//div[@class="profile-about profile-box"]/span/text()').extract()

        if len(manifestos):
            manifestos = manifestos[0]
        else:
            manifestos = 'NULL'
        return manifestos.strip()
