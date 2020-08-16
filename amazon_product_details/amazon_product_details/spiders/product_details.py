import scrapy
from ..items import AmazonProductDetailsItem


class ProductDetailsSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
    'https://www.amazon.com/s?k=men+sunglasses&rh=n%3A2474995011&dc&crid=XLVE97QICI5S&qid=1597578334&rnid=2941120011&sprefix=men+s%2Caps%2C982&ref=sr_nr_n_1'
    ]

    def parse(self, response):
    	items = AmazonProductDetailsItem()

    	product_name = response.css('.a-size-base-plus::text').extract()
    	# product_review = response.css('.a-size-small .a-link-normal .a-size-base').css('::text').extract()
    	product_review = response.css('.a-declarative .aok-align-bottom').css('::text').extract()
    	product_price = response.css('.a-text-normal .a-price-fraction , .a-text-normal .a-price-whole').css('::text').extract()
    	product_imagelink = response.css('.s-image::attr(src)').extract()

    	items['product_name'] = product_name
    	items['product_review'] = product_review
    	items['product_price'] = product_price
    	items['product_imagelink'] = product_imagelink

    	yield items
