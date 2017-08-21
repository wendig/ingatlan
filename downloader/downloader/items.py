# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TestItem(Item):
    # define the fields for your item here like:
	link = Field()
	name = Field()
	
	
	
	
class DetailsItem(Item):
	# stored attributes of a flat
	# todo: more generic solution here 
	
	position 	= Field()
	price 		= Field()
	n_rooms 	= Field()
	floorspace	= Field()
	
	# attributes in the table
	Ingatlan_allapota 	= Field()
	epites_ev			= Field()
	komfort 			= Field()
	energia_tanusitvany = Field()
	emelet 				= Field()
	epulet_szintjei 	= Field() 
	lift 				= Field()
	belmagassag 		= Field()
	futes 				= Field()
	legkondicio 		= Field()
	butorozott 			= Field()
	rezsikoltseg 		= Field()
	min_berleti_ido		= Field()
	akadalymentesitett	= Field()
	furdo_wc 			= Field()
	tajolas 			= Field()
	kilatas 			= Field()
	kertkapcsolatos 	= Field()
	tetoteri 			= Field()
	gepesitett 			= Field()
	kisallat			= Field()
	dohanyzas 			= Field()
	parkolas 			= Field()
	koltozheto			= Field()
	parkolo_dij			= Field()
	erkely				= Field()
	


	
	

