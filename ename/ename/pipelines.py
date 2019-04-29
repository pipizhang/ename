# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import MySQLdb as db

class EnamePipeline(object):
    def process_item(self, item, spider):
        #print(item)
        return item

class StorePipeline(object):

    def __init__(self):
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_pass = os.getenv("DB_PASS")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")

        self.con = db.connect(db=db_name, user=db_user, passwd=db_pass, host=db_host, port=int(db_port))
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        print(item)
        sql = "insert IGNORE into english_name (ename, cname, pronunciation, cname_ext, gender, origin, moral, meaning, impression, similar, created_at) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
        self.cur.execute(sql, (item['ename'], item['cname'], item['pronunciation'], item['cname_ext'], item['gender'], item['origin'], item['moral'], item['meaning'], item['impression'], item['similar']))
        self.con.commit()
        return item
