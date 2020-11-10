# Data Analysis Regarding the Purchase of Supplies from an Ecuadorian Hospital

This project is based in public data that is available via the hospital website and other portals.

The following analysis is based in two specific processes "Subasta the inversa electrónica" and "Regimen Especial."

We wanted to identify:
 - The type of suppliers (Individual or companies) per contract.
 - The increase of expenses per annum since 2017 through the first half of 2020.
 - Time analysis of expenses for the remainder of the year.
 
The steps in obtaining data are as follows:
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
 - newgraphics.ipynb: displays the graphs of the analysis. https://github.com/eluzuriaga83/hagp-corruption/blob/master/scripts/newgraphics.ipynb
 
