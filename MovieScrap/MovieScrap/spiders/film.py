import scrapy


class FilmSpider(scrapy.Spider):
    name = 'film'
    start_urls = ['https://www.afilmywap.surf/']

    def parse(self, response):
        title = response.css('a.cl::attr(title)').getall()
        #print(len(title))
        if response.css('a.cl'):
            href = response.css('a.cl::attr(href)').getall()
        #print(len(href))
        if href:
            for link in href:
               yield scrapy.Request(link,self.parse2)
    
        
    

    def parse2(self, response):
        #print(response)       
        if response.css('a.fileName'):
            img = response.css('.fileName img::attr(src)').getall()
            names = response.css('a.fileName::attr(title)').getall()
            links = response.css('a.fileName::attr(href)').getall()
            source = response.css('.fileName span::text').getall()
            for i in range(len(names)):
                #print(names[i])
                #print(links[i])
                yield{

                    'Name' : names[i],
                    'Link' : links[i],
                    'Source' : source[i],
                    'Image': img[i],
                }



            if response.css('a[rel="next"]'):
                nextpage = response.css('a[rel="next"]::attr(href)').get()
                #print("\tnext page url : ",nextpage)
                if nextpage is not None:
                    yield scrapy.Request(nextpage,self.parse2)
        

        if response.css('a.cl'):
           
            href = response.css('a.cl::attr(href)').getall()
            for link in href:
                yield scrapy.Request(link,self.parse3)
        




    def parse3(self, response):
        #print("\t",response)       
        if response.css('a.fileName'):
            img = response.css('.fileName img::attr(src)').getall()
            names = response.css('a.fileName::attr(title)').getall()
            links = response.css('a.fileName::attr(href)').getall()
            source = response.css('.fileName span::text').getall()
            for i in range(len(names)):
                #print(names[i])
                #print(links[i])
                yield{
                    'Name' : names[i],
                    'Link' : links[i],
                    'Source' : source[i],
                    'Image': img[i],
                }

            if response.css('a[rel="next"]'):
                nextpage = response.css('a[rel="next"]::attr(href)').get()
                #print("\tnext page url : ",nextpage)
                if nextpage is not None:
                    yield scrapy.Request(nextpage,self.parse3)

            

        
        if response.css('a.cl'):
            href = response.css('a.cl::attr(href)').getall()    
            for link in href:
                yield scrapy.Request(link,self.parse4)


    def parse4(self, response):
        if response.css('a.fileName'):
            img = response.css('.fileName img::attr(src)').getall()
            names = response.css('a.fileName::attr(title)').getall()
            links = response.css('a.fileName::attr(href)').getall()
            source = response.css('.fileName span::text').getall()
            for i in range(len(names)):
                #print(names[i])
                #print(links[i])
                yield{
                    'Name' : names[i],
                    'Link' : links[i],
                    'Source' : source[i],
                    'Image': img[i],
                }



            if response.css('a[rel="next"]'):
                nextpage = response.css('a[rel="next"]::attr(href)').get()
                #print("\tnext page url : ",nextpage)
                if nextpage is not None:
                    yield scrapy.Request(nextpage,self.parse3)