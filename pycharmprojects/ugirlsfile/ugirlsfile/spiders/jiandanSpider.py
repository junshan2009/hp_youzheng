# !/usr/bin/env python
# -*-coding:utf-8 -*-

import scrapy
from ugirlsfile.items import UgirlsfileItem

import time
class MeizituSpider(scrapy.Spider):
    name = "Meizitu"
    start_urls = ["https://www.ugirl.com/meinvtupian/6874.html"]
    last_url = []
    with open('url.txt', 'r') as fp:
        crawl_urls = fp.readlines()
        for start_url in crawl_urls:
            last_url.append(start_url.strip('\n'))
    start_urls.append("".join(last_url[-1]))


    def parse(self, response):
        selector = scrapy.Selector(response)
        #item = CrawlmeizituItemPage()

        next_pages = selector.xpath('//*[@id="wp_page_numbers"]/ul/li/a/@href').extract()
        next_pages_text = selector.xpath('//*[@id="wp_page_numbers"]/ul/li/a/text()').extract()
        all_urls = []
        if '下一页' in next_pages_text:
            next_url = "http://www.meizitu.com/a/{}".format(next_pages[-2])
            with open('..//url.txt', 'a+') as fp:
                fp.write('\n')
                fp.write(next_url)
                fp.write("\n")
            request = scrapy.http.Request(next_url, callback=self.parse)
            time.sleep(2)
            yield request

        all_info = selector.xpath('//h3[@class="tit"]/a')
        #读取每个图片夹的连接
        for info in all_info:
            links = info.xpath('//h3[@class="tit"]/a/@href').extract()
        for link in links:
            request = scrapy.http.Request(link, callback=self.parse_item)
            time.sleep(1)
            yield request


    def parse_item(self, response):
         item = UgirlsfileItem()
         selector = scrapy.Selector(response)
         image_url = selector.xpath('//h2/a/@href').extract()
         item['url'] = image_url
         print(item)
         time.sleep(1)
         yield item

