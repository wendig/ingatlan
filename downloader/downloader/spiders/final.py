# -*- coding: utf-8 -*-

# to run: scrapy crawl houses -o items.csv -t csv
# start url-be beleirhatom az elso tiz oldalt egy for ciklussal, izi

import scrapy
from downloader.items import DetailsItem

class QuotesSpider(scrapy.Spider):
	name = "houses"
	

	start_urls = [ 'https://ingatlan.com/budapest/kiado+lakas?page=' + str(x) for x in range(1,2) ] # low number here for testing purposes	
	
	#start_urls = ['https://ingatlan.com/budapest/kiado+lakas?page=1']
	
	# this function extract links of flats on the search page then calls parse_details function on them
	def parse(self, response):
		items = []

		for quote in response.xpath('//a[@class="listing__thumbnail js-listing-active-area" and @title="Részletek"]/@href').extract():
			result = scrapy.Request("https://"+"ingatlan.com/"+quote,callback=self.parse_details)
			items.append(result)
			#todo: append link or id
		return items
		
	
	
	# extracts detailed information about the flats
	# first chunk of information is in table format, then gather the information from photo-header
	def parse_details(self, response):
		item = DetailsItem()
		
		# dictionary from names at the webpage to item fieldname, no whitespace no accent(éáő)...
		# example: 
		dict = {"Légkondicionáló":"legkondicio",                                                                                                                                                                                         
				"Ingatlan állapota":"Ingatlan_allapota",                                                                                                                                                                                 
				"Építés éve":"epites_ev",                                                                                                                                                                                                
				"Emelet":"emelet",                                                                                                                                                                                                       
				"Tetőtér":"tetoteri",                                                                                                                                                                                                    
				"Épület szintjei":"epulet_szintjei",                                                                                                                                                                                     
				"Belmagasság":"belmagassag",                                                                                                                                                                                             
				"Komfort":"komfort",                                                                                                                                                                                                     
				"Dohányzás":"dohanyzas",                                                                                                                                                                                                 
				"Fürdő és WC":"furdo_wc",                                                                                                                                                                                                
				"Parkolóhely ára":"parkolo_dij",                                                                                                                                                                                         
				"Kisállat":"kisallat",                                                                                                                                                                                                   
				"Rezsiköltség":"rezsikoltseg",                                                                                                                                                                                           
				"Bútorozott":"butorozott",                                                                                                                                                                                               
				"Kertkapcsolatos":"kertkapcsolatos",                                                                                                                                                                                     
				"Lift":"lift",                                                                                                                                                                                                           
				"Akadálymentesített":"akadalymentesitett",                                                                                                                                                                               
				"Min. bérleti idő":"min_berleti_ido",                                                                                                                                                                                    
				"Költözhető":"koltozheto",                                                                                                                                                                                               
				"Erkély":"erkely",                                                                                                                                                                                                       
				"Fűtés":"futes",                                                                                                                                                                                                         
				"Kilátás":"kilatas",                                                                                                                                                                                                     
				"Gépesített":"gepesitett",                                                                                                                                                                                               
				"Tájolás":"tajolas",                                                                                                                                                                                                     
				"Energiatanúsítvány":"energia_tanusitvany",                                                                                                                                                                              
				"Parkolás":"parkolas"}

		# get the rows of the table
		rows = response.xpath('//div[@class="paramterers"]/table/tr')
		
		for row in rows:
			#get the name of attribute
			name_on_web = row.xpath('td[1]/text()').extract_first()
			# get its value
			item[ dict[name_on_web] ] = row.xpath('td[2]/text()').extract_first()

		# extract the rest
		item['position'] = response.xpath('//header[@class="photo-header"]/span[@class="photo-address"]/text()').extract_first()
		
		parameters = response.xpath('//div[@class="photo-parameters"]/span[@class="parameter"]/text()').extract()
		item['price'] = parameters[0]
		item['n_rooms'] = parameters[1]
		item['floorspace'] = parameters[2]

		return item
