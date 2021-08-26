import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['http://www.whiskyshop.com/scotch-whisky']

    def parse(self, response):
        for items in response.xpath("//div[@class='product-item-info']"):
            try:
                yield {
                     'product' :items.xpath(".//a[@class='product-item-link']/text()").get(),
                      'price' : items.xpath(".//span[@class='price']/text()").get().replace("£",""),
            # link = items.xpath("//a[@class='product-item-link']/@href").extract_first()
                      'link' : items.xpath(".//a[@class='product-item-link']").attrib['href'],

                }
            except:
                yield {
                    'product' :items.xpath(".//a[@class='product-item-link']/text()").get(),
                    'price' : "Sold OUT",

                    'link'  : items.xpath(".//a[@class='product-item-link']").attrib['href']
                }

        next_page = response.xpath("//a[@class='action  next']/@href").extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


