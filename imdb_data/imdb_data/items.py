# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
            Title=scrapy.Field()
                        
            releaseYear=scrapy.Field()
            desc1=scrapy.Field()
            Meta_score=scrapy.Field()
            rating=scrapy.Field()
            vote=scrapy.Field()
            image=scrapy.Field()
            duration=scrapy.Field()
            rated=scrapy.Field()
