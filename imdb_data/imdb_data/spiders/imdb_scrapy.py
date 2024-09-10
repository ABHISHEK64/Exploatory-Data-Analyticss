import scrapy
import json
from ..items import ImdbDataItem
from selenium import webdriver
from scrapy_selenium import SeleniumRequest
from scrapy_playwright.page import PageMethod
import re

scrapy_script = """
    
    
    // Function to scroll up and down 50 times and then click a button
function scrollAndClick(buttonSelector, scrollTimes) {
    let scrollCount = 0;
    const scrollInterval = setInterval(() => {
        // Scroll down by 500 pixels
        window.scrollBy(0, document.body.scrollHeight);

        setTimeout(() => {
            // Scroll up by 500 pixels
            
            const button = document.querySelector(buttonSelector);
             if (button) {
                    button.click();
                } else {
                    console.error('Button not found!');
                }
                scrollCount++
            
          window.scrollBy(document.body.scrollHeight, 0);
             if(scrollCount>scrollTimes){
                clearInterval(scrollInterval)
             }  
        }, 500); // Adjust this timeout as needed to control the speed of scrolling
    }, 1000); // Adjust this interval as needed to control the speed of scrolling
}

// Call the function to scroll 50 times and then click the button with the given selector
scrollAndClick('span.ipc-see-more__text', 10000000);

    
"""

class Quetes_spider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                meta={
                    'playwright': True,
                    'playwright_include_page': True, 
            
                    'playwright_page_methods': [
                        PageMethod("evaluate", scrapy_script),

                        PageMethod("wait_for_timeout", 999999),
                        PageMethod("new_context", {"timeout": 36000}),
                        PageMethod("wait_for_selector", "li.ipc-metadata-list-summary-item")
                    ]
                }
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        
        #await page.close()  # Uncomment this if you want to close the page
        
        movies_info = ImdbDataItem()
        movies_data = response.css('li.ipc-metadata-list-summary-item')
        print(len(movies_data))
        
        for movie in movies_data:
            Title = movie.css('h3.ipc-title__text::text').extract_first()
            releaseYear = movie.css('span.hCbzGp::text').extract_first()
            duration = movie.css('span.hCbzGp::text').extract()
            rated=movie.css('span.sc-b189961a-8::text').extract()
            if len(rated)>2:
                rated=rated[2]
            else:
                rated='Not Rated'
            if len(duration) > 1:
                duration = duration[1]
            else:
                duration ='Not Relased'
            Meta_score = movie.css('span.bXIOoL::text').extract_first()
            rating = movie.css('span.ipc-rating-star--rating::text').extract_first()
            vote=movie.css('span.ipc-rating-star--voteCount::text').extract()
            if len(vote)>1:
                vote=vote[1]
            else:
                vote = [v.replace("\xa0(", '').replace(')','') for v in vote]
                if len(vote)>0:
                    vote=vote[0]
                else:
                    vote=0



            plot = movie.css('div.ipc-html-content-inner-div::text').extract_first()
            img = movie.css("img.ipc-image").xpath("@src")
            imageURL = img.extract_first()

            movies_info['Title'] = Title
            movies_info['releaseYear'] = releaseYear
            movies_info['desc1'] = plot
            movies_info['Meta_score'] = Meta_score
            movies_info['duration'] = duration
            movies_info['rating'] = rating 
            movies_info['image'] = imageURL
            movies_info['vote'] =vote
            movies_info['rated']=rated

            yield movies_info
