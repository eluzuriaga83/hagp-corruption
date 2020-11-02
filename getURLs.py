import scrapy
import re
from scrapy.selector import Selector 

from scrapy.crawler import CrawlerProcess

class PdfDocument(scrapy.Spider):
    name = 'hospital_documents'

    # Punto de partida
    start_urls = ['https://www.hagp.gob.ec/index.php/transparencia']
    
    # What we're going to do after the page is resolved
    def parse(self, response):
        # We yield a dict of this
        result = {}
        years = {
            "2020": "1",
            "2019": "4",
            "2018": "5",
            "2017": "6",
            "2016": "7"
        }

        monthsdic = {
            "ENERO": "1",
            "FEBRERO": "2",
            "MARZO": "3",
            "ABRIL": "4",
            "MAYO": "5",
            "JUNIO": "6",
            "JULIO": "7",
            "AGOSTO": "8",
            "SEPTIEMBRE": "9",
            "OCTUBRE": "10",
            "NOVIEMBRE": "11",
            "DICIEMBRE": "12",
        }

        for index in range(2,11,2): #years (2,4,6,8,10)
            main_xpath = "//div[@id='lof-accordion233']/div[{0}]".format(index)
            # Year of the file 
            year = response.xpath("{0}/div/h4/text()".format(main_xpath)).get().split()[1]
            months = response.xpath("{0}/div/div[1]/div/div[1]/a/text()".format(main_xpath)).getall()
          
            #result[year] = months
            index = 0
            while index < len(months):
                 months[index] = re.sub('[^A-Za-z0-9]+', '', months[index])
                 index += 1
                             
            
            for month in months:
                idfor_div = years[year] + "-" + monthsdic[month] + "-" + month.lower()
                actual_month = month
                #//div[@id='5-4-abril']
                accordion_groups = "//div[@id='" + idfor_div + "']"
                distributivo_personal = response.xpath(accordion_groups + "//a[6]/@href").get()
                remuneracion_mensual = response.xpath(accordion_groups + "//a[7]/@href").get()
                procesos_contrataciones = response.xpath(accordion_groups + "//a[14]/@href").get()
  
                yield {
                            "year": year,
                            "month": actual_month,
                            "distributivo_personal": distributivo_personal,
                            "remuneracion_mensual": remuneracion_mensual,
                            "procesos_contrataciones": procesos_contrataciones
                        }        
                     
            
            
         
            

#process = CrawlerProcess(settings={
# "FEEDS": {r'D:\ICD\Proyecto\files.json': {"format": "json"}}})
process = CrawlerProcess(settings={

    'FEED_FORMAT': "json",
    'FEED_URI': "pdfurls.json"
})
process.crawl(PdfDocument)
response = process.start()