# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser, parse_new_url
from ..items import ZillowFinalItem
import json


class HousesSpider(scrapy.Spider):
    name = 'houses'
    allowed_domains = ['www.zillow.com']

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback = self.parse,
            cookies = cookie_parser(),
            meta = {
                'currentPage':1
            }
        )

    def parse(self, response):
        current_page = response.meta['currentPage']
        json_resp = json.loads(response.body)
        houses = json_resp.get('cat1').get('searchResults').get('listResults')
        for house in houses:
            loader = ItemLoader(item=ZillowFinalItem())
            loader.add_value('id', house.get('id'))
            loader.add_value('status_type', house.get('statusType'))
            loader.add_value('status_text', house.get('statusText'))
            loader.add_value('price', house.get('price'))
            loader.add_value('address', house.get('address'))
            loader.add_value('city', house.get('addressCity'))
            loader.add_value('state', house.get('addressState'))
            loader.add_value('zipcode', house.get('addressZipcode'))
            loader.add_value('area_sqft', house.get('area'))
            loader.add_value('latitude', house.get('latLong').get('latitude'))
            loader.add_value('longitude', house.get('latLong').get('longitude'))
            loader.add_value('broker_name', house.get('brokerName'))
            loader.add_value('broker_phone', house.get('brokerPhone'))

            yield loader.load_item()

        total_pages = json_resp.get('cat1').get('searchList').get('totalPages')
        if current_page <= total_pages:
            current_page+=1 
            yield scrapy.Request(
                url = parse_new_url(URL, page_number=current_page),
                callback=self.parse,
                cookies=cookie_parser(),
                meta={
                    'currentPage': current_page
                }
            )