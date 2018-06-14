# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .sql import Sql
from movies.items import MoviesItem
class MoviesPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,MoviesItem):
            movie_name = item['movie_name']
            movie_info = item['movie_info']
            movie_download = item['movie_download']
            Sql.insert(movie_name, movie_info,movie_download)
            print("保存成功")