BOT_NAME = 'animal_subspecies'

SPIDER_MODULES = ['animal_subspecies.spiders']
NEWSPIDER_MODULE = 'animal_subspecies.spiders'

ITEM_PIPELINES = {
    'animal_subspecies.pipelines.AnimalSubspeciesImagePipeline': 1,
}


IMAGES_STORE = 'images'  # Replace with the path where you want to store images
