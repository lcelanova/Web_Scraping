import scrapy

class WorldometerSpider(scrapy.Spider):
    name = 'worldometer'
    allowed_domains = ['www.worldometers.info']
    #el protocolo http se incluye automaticamente hay que añadir la s de seguridad si la página que hemos elegido la tiene
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        rows = response.xpath('//tr')

        for row in rows:
            #title = response.xpath('//h1/text()').get()
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()

            yield {
                #'titles': title,
                'countries': countries,
                'population': population
            }

"""
yield funciona igual que return pero permite 

devolver un valor sin destruir el valor de sus variables locales

para buscar multiples elementos response.xpath().getall()

para buscar un elemento response.xpath().get()
"""