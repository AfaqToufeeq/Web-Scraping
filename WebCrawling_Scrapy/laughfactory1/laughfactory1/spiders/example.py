import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jokes'
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes']

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            text = joke.xpath("normalize-space(.//div[@class='joke-text']/p/text())").get()
            yield {
                'jokes_text': text
            }

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if "laughfactory" in next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

