# import scrapy
# #Scrapy
# #<div id='some-id'>
# #     <a href='www.example.com'>Link</a>
# # </div>
#
# # 1. //div/a     --> to select all a(anchors) in a div  --->  <a href='www.example.com'>Link</a>
# # 2. //div/a/text()  --> to select text of anchor
# # 3. //div/a/@href --> to select link like www.google.com
#
# # <p id='some-id'> paragraph1 </p>
# # <p class='some-Clas' paragraph 2 </p>
# #
# # 1. to get any node based on id or class
# #     //p[@id='some-id'] --> <p id='some-id'> paragraph1 </p>
# #     //p[@class='some-class'] --> <p id='some-id'> paragraph2 </p>
# class jokesSpider(scrapy.Spider):
#     name='jokes'
#
#     start_urls = [
#         'http://www.laughfactory.com/jokes/family-jokes'
#     ]
#
#     def parse(self, response):
#         for joke in response.xpath("//div[@class='jokes]"):
#             yield {
#                 'jokes_text': joke.xpath(".//div[@class='joke-text]/p").extract_first()
#             }
#
#
#         next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
#         if next_page is not None:
#             next_page_link = response.urljoin(next_page)
#
#             yield scrapy.Request(url=next_page_link, callback=self.parse)
