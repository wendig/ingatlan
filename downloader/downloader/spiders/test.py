# -*- coding: utf-8 -*-

# to run: scrapy crawl quotes -o items.csv -t csv
# start url-be beleirhatom az elso tiz oldalt egy for ciklussal, izi


import scrapy
from downloader.items import TestItem

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	

	start_urls = [ 'https://ingatlan.com/budapest/kiado+lakas?page=' + str(x) for x in range(1,2) ] # low number here for testing purposes	
	
	#start_urls = ['https://ingatlan.com/budapest/kiado+lakas?page=1']

	def parse(self, response):
		items = []
		
		#<main class="resultspage__main">
		
		for quote in response.xpath('//a[@class="listing__thumbnail js-listing-active-area" and @title="Részletek"]/@href').extract():
			item = TestItem()
			
			#item['link'] = quote.xpath('//a[@class="listing__thumbnail js-listing-active-area"]/@href').extract_first()
			
			item['link'] = quote 
			item['name'] = "ahh"
			
			#response.xpath('//a[contains(@href, "image")]/@href').extract()
			#response.xpath('//div[@id="images"]/a/text()').extract_first()
			
			
			#item['text'] = quote.css('span.text::text').extract_first()
			#item['author'] = quote.css('small.author::text').extract_first()
			#item['tags'] = quote.css('div.tags a.tag::text').extract()

			items.append(item)
		
		
		
		return items