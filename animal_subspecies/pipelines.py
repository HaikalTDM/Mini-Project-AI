from scrapy.pipelines.images import ImagesPipeline
import scrapy

class AnimalSubspeciesImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        item['images'] = [x['path'] for ok, x in results if ok]
        return item
