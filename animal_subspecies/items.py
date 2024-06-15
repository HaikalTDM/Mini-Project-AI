import scrapy

class AnimalSubspeciesItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
