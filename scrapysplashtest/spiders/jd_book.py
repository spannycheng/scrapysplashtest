# -*- coding: utf-8 -*-
# import scrapy
#
#
# class JdBookSpider(scrapy.Spider):
#     name = 'jd_book'
#     allowed_domains = ['jd.com']
#     start_urls = ['http://jd.com/']
#
#     def parse(self, response):
#         pass
# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from scrapysplashtest.items import PyBooksItem

lua_script ='''
function main(splash)
    splash:go(splash.args.url)
    splash:wait(2)
    splash:runjs("document.getElementsByClassName('pn-next')[0].scrollIntoView(true)")
    splash:wait(2)
    return splash.html()
end
'''
class JDBookSpider(scrapy.Spider):
    name = "jd_book"
    allowed_domains = ['search.jd.com']
    base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python'
    def start_requests(self):
        yield Request(self.base_url,callback=self.parse_urls,dont_filter=True)
    def parse_urls(self,response):
        for i in range(20):
            url = '%s&page=%s' % (self.base_url,2*i+1)
            yield SplashRequest(url,
                                endpoint='execute',
                                args={'lua_source':lua_script},
                                cache_args=['lua_source'])
    def parse(self, response):

        for sel in response.css('ul.gl-warp.clearfix>li.gl-item'):
            pyjdbooks = PyBooksItem()
            pyjdbooks['name'] = sel.css('div.p-name').xpath('string(.//em)').extract_first()
            pyjdbooks['comment']=sel.css('div.p-commit').xpath('string(.//a)').extract_first()
            pyjdbooks['promo_words']=sel.css('div.p-name').xpath('string(.//i)').extract_first()
            print(pyjdbooks)
            print("="*60)
            yield pyjdbooks
