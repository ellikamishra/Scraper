# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo

# class Web1Pipeline:
#     def __init__(self):
# 		self.conn = pymongo.MongoClient(
# 			'localhost',
# 			27017
# 		)
# 		db = self.conn['ngo']
# 		self.collection = db['demo']

# 	def process_item(self, item, spider):
# 		self.collection.insert(dict(item))
# 		return item

class NgoPipeline:
	def __init__(self):
		self.conn=pymongo.MongoClient(
			'localhost',
			27017
		)
		db=self.conn['ngo']
		self.collection=db['demo']
	def process_item(self,item,spider):
		self.collection.insert(dict(item))
		return item
