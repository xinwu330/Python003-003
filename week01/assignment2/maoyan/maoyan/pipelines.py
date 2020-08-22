# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd


class MaoyanPipeline:
    def process_item(self, item, spider):
        print('hahaha')
        print(item)
        movie_name = item['movie_name']
        movie_types = item['movie_types']
        movie_release_date = item['movie_release_date']
        output = f'|{movie_name}|\t|{movie_types}|\t|{movie_release_date}|\n\n'
        with open('./top10_movie_infos_02.csv', 'a+', encoding='utf_8_sig') as f:
            f.write(output)
        return item