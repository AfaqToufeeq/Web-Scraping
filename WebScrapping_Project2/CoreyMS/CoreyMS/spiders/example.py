import scrapy

class SpiderCoreyMS(scrapy.Spider):
    name = "CoreMS"
    start_urls = ['http://coreyms.com']

    def parse(self, response):
        title = response.xpath(".//p[@class='site-description']/text()").get()
        #heading = response.xpath("(.//h2[@class='entry-title']/a)[2]/text()").get()    //---> to pick one entity
        summary = response.xpath("//div[@class='entry-content']/p/text()")
        # video_link = str(response.xpath("(//iframe[@class='youtube-player']//@src)").extract())
        # vid_id = video_link.split('/')[4]
        # vid_id = vid_id.split('?')[0]
        # yt_link = f'https://www.youtube.com/watch?v={vid_id}'
        # yield {
        #     # 'title' : title,
        #     # 'summary' : summary,
        #     'video_link' : yt_link
        # }

        for i in response.xpath("//article"):
            heading = i.xpath(".//h2[@class='entry-title']/a/text()").get()
            summary = i.xpath(".//div[@class='entry-content']/p/text()").get()

            try:
                video_link = str(response.xpath("(//iframe[@class='youtube-player']//@src)").extract())
                vid_id = video_link.split('/')[4]
                vid_id = vid_id.split('?')[0]
                yt_link = f'https://www.youtube.com/watch?v={vid_id}'
            except Exception as e:
                yt_link = None

            yield {
                # 'title': title,
                'Heading': heading,
                'Summary': summary,
                'Video-Link': yt_link
            }