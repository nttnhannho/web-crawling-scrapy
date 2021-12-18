# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import mysql.connector
import pymongo


class QuotetutorialPipeline:
    def __init__(self):
        self.conn = None
        self.collection = None
        self.create_connection()
        # self.create_table()  # this function is only for sqlite3 & mysql

    def create_connection(self):
        # self.conn = sqlite3.connect("myquote.db")  # sqlite3
        # self.conn = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="myquote")  # mysql
        # self.curr = self.conn.cursor()  # sqlite3 & mysql
        self.conn = pymongo.MongoClient("localhost", 27017)  # mongdb
        db = self.conn["myquote"]  # mongdb
        self.collection = db["quote_tb"]  # mongdb


    # def create_table(self):  # this function is only for sqlite3 & mysql
    #     self.curr.execute("""drop table if exists quote_tb""")
    #     self.curr.execute("""create table quote_tb(
    #                             title text,
    #                             author text,
    #                             tag text
    #                             )""")

    def process_item(self, item, spider):
        # self.store_db(item)  # sqlite3 & sql
        self.collection.insert_one(dict(item))
        return item

    # def store_db(self, item):  # this function is only for sqlite3 & mysql
    #     # self.curr.execute("""insert into quote_tb values (?, ?, ?)""", (
    #     #                     item["title"][0],
    #     #                     item["author"][0],
    #     #                     item["tag"][0]
    #     #                 ))  # sqlite3
    #     self.curr.execute("""insert into quote_tb values (%s, %s, %s)""", (
    #                             item["title"][0],
    #                             item["author"][0],
    #                             item["tag"][0]
    #                         ))  # mysql
    #     self.conn.commit()

