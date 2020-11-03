# Data Analytics for the purchase of supplies from a hospital 

# Data Analisis of the purchase of supplies from a Ecuador hospital.

This project is based in public data that is available in the hospital website and other portals.

The following analysis is based in two specific processes "Subasta the inversa electrónica" and "Regimen Especial"

We wanted to identify:
 - The type of suppliers (Individual or companies) per contract.
 - The increase of expenses between each year since 2017 to first semester of 2020
 - Time analysis of the year with more expenses.
 
The steps to get the information are the following:
 - Downloading pdfs from the hospital Website to extract data
 - Creation of scrapping to get information from the webiste http://compraspublicas.gob.ec/
 - Cleaning and transformation of the data
 - Visualization
 

The libraries used:
 - Pandas
 - Seaborn
 
 Scripts:
 - get-urls.ipynb: get the urls of the following pdfs: distributivo_personal, remuneracion_mensual, procesos_contrataciones
 - download-pdfs.ipynb: donwload the pdfs from the urls that we got running the program get-urls 
 - search-processSIE.ipynb: get all the information related to process Subasta Inversa Electrónica.
 - search-processRE.ipynb: get all the information related to process Regimen Especial.
 - concat_allfiles.ipynb: concat all the files per year 
 - get-alldata.ipynb: get additional information for the process "Regimen Especial" and "Subasta Inversa Electrónica" from the records which status is "Adjudicado" 
 - newgraphics.ipynb: displays the graphs of the analysis.
 
