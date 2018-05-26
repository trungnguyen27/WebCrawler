
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hcmreal.items import HcmrealItem
from scrapy_splash import SplashRequest

titleDict = {
        u'Tình trạng pháp lý':'legal_status',
        u'Diện tích': 'area',
        u'Hướng' : 'direction',
        u'Số tầng': 'num_of_floor',
        u'Phòng ngủ': 'bedrooms',
        u'Phòng tắm': 'bathrooms',
        u'Đường trước nhà': 'front_street_length',
        u'Thuộc dự án': 'project'
        }
    
class ElectronicsSpider(CrawlSpider):
    name = 'hcmrealspyder'
    allowed_domains = ['www.muabannhadat.vn']
    start_urls = [
        'http://www.muabannhadat.vn/nha-ban-3513/tp-ho-chi-minh-s59',
    ]
    
    print ("Setting rules")
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagination > li > a#MainContent_ctlList_ctlResults_ctlPager_lnkNext',)),
             callback="parse_item",
             follow=True),)
    print("finished Setting Rules")
    def parse_item(self, response):
        item_links = response.css('.title > div > a::attr(href)').extract()
        for a in item_links:
            url = 'http://www.muabannhadat.vn'+a
            #yield PhantomJSDownloadHandler.download_request('http://www.muabannhadat.vn'+a, self.parse_detail_page)
            # yield scrapy.Request('http://www.muabannhadat.vn'+a, callback=self.parse_detail_page)
            yield SplashRequest(url, self.parse_detail_page,
                                endpoint='render.html',
                                args={'wait':0.5})
    def parse_detail_page(self, response):
        print("Parsing detail page started")
        if(response.url == ''):
            print("Empty URL")
            yield

        print("Collecting at " + response.url)
        tables = response.css('table')
        items = tables[0].css('tr')
        realItem = HcmrealItem()
        realItem['price'] = response.css('span#MainContent_ctlDetailBox_lblPrice::text').extract()
        realItem['title'] = response.css('h1::text').extract()[0].strip()
        realItem['house_type'] = response.css('.title-detail-page > .pull-left > .seo-category-detail-page::text').extract()[0].strip()
        realItem['district'] = response.css('span#MainContent_ctlDetailBox_lblDistrict > a::text').extract()[0]
        realItem['url'] = response.url
        print("DISTRICT " + realItem['district'])
        for i, item in enumerate(items):
            title = item.css('th::text').extract()[0].strip()
            content = item.css('td>span::text').extract()
            if content and len(content)>= 1:
                content = content[0].strip()
            realItem[titleDict[title]] = content
        try:
            if 'price' in realItem and 'area' in realItem and 'bedrooms' in realItem:
                yield realItem
        except:
            print("error")
        yield realItem

      

            
             