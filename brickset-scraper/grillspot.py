import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    handle_httpstatus_list = [404]
    start_urls = ['https://rootways.com/shop/magento-2-mega-menu-extension']
	
    def parse(self, response):
       SET_SELECTOR = '.product-view'
       for brickset in response.css(SET_SELECTOR):
			
           NAME_SELECTOR = 'h1 ::text'
           IMAGE_SELECTOR = 'img ::attr(src)'
           yield {
               'name': brickset.css(NAME_SELECTOR).extract_first(),
               'image': brickset.css(IMAGE_SELECTOR).extract_first(),
           }
