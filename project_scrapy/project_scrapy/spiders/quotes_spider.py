from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         "https://quotes.toscrape.com/page/1/",
    #         "https://quotes.toscrape.com/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    start_urls = [
        "https://quotes.toscrape.com",
    ]

    def parse(self, response):
        quotes = response.css("div.quote")
        # print(f"Quotes:: {quotes}")
             
        # print(f"Text:: {text}")
        
        # print(f"Author:: {author}")
        
        # print(f"Tags:: {tags}")
        
        for quote in quotes:
            # text = quote.css("span.text::text").get()   
            # author = quote.css("small.author::text").get()
            # tags = quote.css("div.tags a.tag::text").getall()
            # print(dict(text=text, author=author, tags=tags))
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     # next_page = response.urljoin(next_page)
        #     # yield scrapy.Request(next_page, callback=self.parse)
        #     yield response.follow(next_page, callback=self.parse)
        for a in response.css("ul.pager a"):
            yield response.follow(a, callback=self.parse)
            
            