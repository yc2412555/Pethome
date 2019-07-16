# -*- coding: utf-8 -*-
import json
import re

import scrapy
from lxml import etree
from scrapy import Request
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pethome.items import PethomeItem
from pethome.settings import DEFAULT_PAGE_COUNT


class PetknowledgeSpider(scrapy.Spider):
    name = 'petknowledge'
    count = 0
    base_url = 'http://www.yc.cn/api/searchPetData.do?petRaceId=2&pageNum={}&pageSize=8&keyword=&baseInfo=&detailInfo='
    total_page = DEFAULT_PAGE_COUNT

    def make_url(self, base_url, total_page):
        urls = []
        for i in range(1, total_page+1):
            complete_url = base_url.format(i)
            print(complete_url)
            urls.append(complete_url)
        return urls

    def get_page_count(self):
        try:
            cat_page_urls = 'http://www.yc.cn/pet/maomao'
            browser = webdriver.Chrome()
            wait = WebDriverWait(browser, 10)
            browser.get(cat_page_urls)
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#laypage_0 > a.laypage_next')
                )
            )
            html = etree.HTML(browser.page_source)
            all_page = html.xpath('//*[@id="laypage_0"]/a[5]/@data-page')
            if len(all_page) > 0:
                self.total_page = int(all_page[0])
            browser.close()
            return self.total_page
        except TimeoutException:
            if self.count > 2:
                raise ConnectionError("Network error")
            else:
                self.count += 1
                self.get_page_count()

    def start_requests(self):
        total_page_num = self.get_page_count()
        all_urls = self.make_url(self.base_url, total_page_num)
        for url in all_urls:
            yield Request(url, callback=self.json_parse)

    def clear_dict_info(self, item):
        info = ''
        pat = re.compile('<.*?>', re.S)
        if isinstance(item, dict):
            for key, value in item.items():
                new_val = re.sub(pat, '', value)
                info = info + key + ':' + new_val
        else:
            info = re.sub(pat, '', item)
        return info

    def json_parse(self, response):
        results = json.loads(response.text.lstrip('(').rstrip(')'))
        item = PethomeItem()
        pagesize = len(results['list'])
        for i in range(pagesize):
            item['alias'] = item['en_name'] = item['weight'] = item['origin'] = item['price'] = 'null'
            basedata = results['list'][i]['baseData']
            for data in basedata:
                if data['id'] == "1":
                    item['en_name'] = data['value']
                elif data['id'] == "3":
                    item['origin'] = data['value']
                elif data['id'] == "4":
                    item['weight'] = data['value']
                elif data['id'] == "6":
                    item['price'] = data['value']

            item['cat_vari_name'] = results['list'][i]['name']

            item['cat_vari_img'] = results['list'][i]['showImage']

            item['alias'] = results['list'][i]['alisName']

            item['shape'] = results['list'][i]['bodyType']

            item['cat_habit'] = self.clear_dict_info(results['list'][i]['breedInfo'].get('生活习性', 'null'))

            # item['cat_character'] = self.clear_dict_info(results['list'][i]['breedInfo'].get('性格特点', 'null'))

            item['sti_degree'] = results['list'][i]['detail'][7]['value']

            item['bar_degree'] = results['list'][i]['detail'][1]['value']

            item['hair_loss_degree'] = results['list'][i]['detail'][2]['value']

            item['fri_degree'] = results['list'][i]['detail'][0]['value']

            item['ani_fri_degree'] = results['list'][i]['detail'][0]['value']

            item['trainability'] = results['list'][i]['detail'][11]['value']

            item['city_degree'] = results['list'][i]['detail'][5]['value']

            item['feature'] = self.clear_dict_info(results['list'][i]['breedInfo'].get('形态特征及鉴别', 'null'))

            item['attention'] = results['list'][i]['attentionInfo']
            if len(item['attention']) > 0:
                item['attention'] = self.clear_dict_info(item['attention'])
            else:
                item['attention'] = 'null'

            item['nurturing_knowledge'] = results['list'][i]['feedInfo']
            if len(item['nurturing_knowledge']) > 0:
                item['nurturing_knowledge'] = self.clear_dict_info(item['nurturing_knowledge'])
            else:
                item['nurturing_knowledge'] = 'null'

            yield item



