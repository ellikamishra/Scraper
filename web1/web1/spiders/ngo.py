import scrapy
import re
import string
from ..items import NgoItem

class NgoSpider(scrapy.Spider):
    name='ngo'
    start_urls=['https://ngosindia.org/karnataka/bengaluru-bangalore-ngos/']

    def parse(self,response):
        url=response.css('ul.lcp_catlist a::attr(href)').extract()
        for item in url:
            yield response.follow(item,callback=self.parse_dir_contents)
    def parse_dir_contents(self,response):
        
        other="".join(response.xpath("//div[@class = 'npos-postcontent clearfix']/p/text()").extract())
        # print(other)
        dict1={}
        # for e in other:
        #     print(e)
            # if(e=="Email"):
            #     e+=e.strip()
            #     e=e.replace("\n","")
            #     print("email",e)
                
        
        start=other.find("Email")
        end=other.find(" \n",start)
        if len(other[start:end])>6 and len(other[start:end])<100:
            dict1['info']=other[start:end]
        

        yield NgoItem(**dict1)