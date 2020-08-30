# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_types = item['movie_types']
        movie_release_date = item['movie_release_date']


        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='test1234',
                             db='maoyan',
                             charset='utf8mb4',
                             port= 3306)
        cur = connection.cursor()

        try:
            # Create a new record
            sql = "INSERT INTO `movies` (`name`, `types`, `release_date`) VALUES (%s, %s, %s)"
            cur.execute(sql, (movie_name, movie_types, movie_release_date))
            # cur.close()
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except Exception as err:
            print(err)
            connection.rollback()
        
        connection.close()
        return item