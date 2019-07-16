# -*- coding: utf-8 -*-
import json
import re

import scrapy
from lxml import etree
from scrapy import Request, Selector
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
    cat_detail_baseurl = 'http://www.yc.cn/pet/breed-{}.html'
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

    # def clear_dict_info(self, item):
    #     info = ''
    #     pat = re.compile('<.*?>', re.S)
    #     if isinstance(item, dict):
    #         for key, value in item.items():
    #             new_val = re.sub(pat, '', value)
    #             info = info + key + ':' + new_val
    #     else:
    #         info = re.sub(pat, '', item)
    #     return info

    def cat_photo_parse(self, response):
        item = PethomeItem()
        sel = Selector(response)
        item['cat_vari_name'] = sel.xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]/span[2]/text()').extract_first()
        photos = sel.xpath('/html/body/div/div[2]/div[2]/div[2]/div/div[1]//img/@src').extract()
        for i in range(len(photos)):
            item['path'] = photos[i]
            yield item

    def json_parse(self, response):
        results = json.loads(response.text.lstrip('(').rstrip(')'))
        pagesize = len(results['list'])
        count = 0
        for i in range(pagesize):
            count += 1
            if count > 108:
                print(count)
            cat_id = results['list'][i]['petBreedId']
            cat_detail_url = self.cat_detail_baseurl.format(cat_id)
            yield Request(cat_detail_url, callback=self.cat_photo_parse)



