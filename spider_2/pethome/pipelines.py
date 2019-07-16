# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from pethome.settings import MYSQL_HOST, MYSQL_PORT, MYSQL_DB, MYSQL_CAT_TABLE, MYSQL_PHOTO_TABLE


class PethomePipeline(object):

    def __init__(self):
        self.host = MYSQL_HOST
        self.port = MYSQL_PORT
        self.db = MYSQL_DB
        self.cat_table = MYSQL_CAT_TABLE
        self.photo_table = MYSQL_PHOTO_TABLE

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host=self.host, port=self.port,
                               user='root', password='123456',
                               database=self.db, charset='utf8')
        self.cursor = self.conn.cursor()
        # print('+++++++++++++++++')
        # print('open')

    def close_spider(self, spider):
        # print('-----------------')
        # print('close')
        self.conn.close()

    def process_item(self, item, spider):
        query_sql = 'select cati_id from {} where cat_vari_name = "{}";'.format(self.cat_table, item['cat_vari_name'])
        # sql = 'insert into {} (cat_vari_name, cat_vari_img, en_name, alias, weight, shape, origin, price, cat_habit, sti_degree, bar_degree, hair_loss_degree, fri_degree, ani_fri_degree, trainability, city_degree, feature, attention, nurturing_knowledge) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", {}, {}, {}, {}, {}, {}, {}, "{}", "{}", "{}");'.format(
        #     self.cat_table, item["cat_vari_name"], item["cat_vari_img"], item["en_name"], item["alias"], item["weight"], item["shape"], item["origin"], item["price"], item["cat_habit"], item["sti_degree"], item["bar_degree"], item["hair_loss_degree"], item["fri_degree"], item["ani_fri_degree"], item["trainability"], item["city_degree"], item["feature"], item["attention"], item["nurturing_knowledge"]
        # )
        self.cursor.execute(query_sql)
        # self.conn.commit()
        result = self.cursor.fetchone()
        catvari_id = result[0]
        insert_sql = 'insert into {} (path, catvari_id) values ("{}", {});'.format(self.photo_table, item['path'], catvari_id)
        self.cursor.execute(insert_sql)
        self.conn.commit()
        return 0
