# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Web1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    pass

class NgoItem(scrapy.Item):
    def __setitem__(self,key,value):
        self._values[key]=value
        self.fields[key]={}
