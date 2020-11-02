import pandas as pd
import gdown
import re
from urllib.parse import urlsplit

data = pd.read_csv('D:\ICD\proyecto\pdfurls.csv') 

def main():

    for index, row in data.iterrows():
        year = row["year"]
        month = row["month"]

        download_PDF(year, month, "distributivo_personal", row["distributivo_personal"])   
        download_PDF(year, month, "remuneracion_mensual", row["remuneracion_mensual"])   
        download_PDF(year, month, "procesos_contrataciones", row["procesos_contrataciones"])            

    

def clear_Link(url):
    r1 = urlsplit(url)
    
    if r1.path == '/open':
        url = url.replace("open", "uc")
       
    else:
        url = 'https://drive.google.com/uc?id='
        path = r1.path.split("/")
        
        for symbol in path:
            if '1' in symbol or '0' in symbol:
              id= symbol
              url = url + id

    return url

def download_PDF(year, month, name, pdflink):
    pdfLink = clear_Link(pdflink)
    #name = re.sub('[^A-Za-z0-9]+', '', reg.columns[index])
    
    output = r"D:\ICD\hagp"+ "/" + str(year) + "/" + name + "-" + str(month) + "-" + str(year) + ".pdf"
    gdown.download(pdfLink, output, quiet=False) 

if __name__ == "__main__":
    main()