import tabula

#Read pdf into list of DataFrame

def processRemuneracionMensualPorPuesto2020(file,outputfile,fecha):
    pages = tabula.read_pdf(file, pages='all')
    print(len(pages))
    for index, page in enumerate(pages):

        #Remove header
        page_data = page.loc[1:]

        # Check if it is the last page. If it is last page, remove last rows (the last rows does not hold any valuable data)
        if index == (len(pages)-1):
            maxFilas = page_data.shape[0]
            page_data = page_data[0:maxFilas-6].dropna(1)

        # Drop all the columns that does not have valid data
        page_data = page_data.dropna(axis=1)

        # Clean the data
        columns = page_data.columns
        print(index)
        page_data[columns[2]] = page_data[columns[2]].apply(lambda x : x.replace("\r", " "))
        page_data[columns[3]] = page_data[columns[3]].apply(lambda x : x.replace("\r", " "))
        page_data[columns[5]] = page_data[columns[5]].apply(lambda x : x.replace("\r", " "))
        page_data[columns[6]] = page_data[columns[6]].apply(lambda x : x.replace("$", "").replace(".","",x.count(".") - 1).strip())
        page_data[columns[7]] = page_data[columns[7]].apply(lambda x : x.replace("$", "").replace(".","",x.count(".") - 1).strip())
        page_data[columns[8]] = page_data[columns[8]].apply(lambda x : x.replace("$", "").strip())
        page_data[columns[9]] = page_data[columns[9]].apply(lambda x : x.replace("$", "").strip())
        page_data[columns[10]] = page_data[columns[10]].apply(lambda x : x.replace("$", "").strip())
        page_data = page_data.drop([columns[0], columns[4]], axis=1)
        page_data.insert(0, 'fecha', fecha)
        page_data = page_data.dropna();
        if index == 0 :
            page_data.to_csv(outputfile,mode='w',index = False, header= ['Fecha',
                                                                             'Empleado',
                                                                             'CARGO',
                                                                             'Regimen laboral',
                                                                            'Grado jerárquico',
                                                                            'Remuneración mensual',
                                                                            'Remuneración unificada (anual)',
                                                                            'Décimo Tercera Remuneración',
                                                                            'Décima Cuarta Remuneración',
                                                                            'Horas suplementarias y extraordinarias',
                                                                        ''])
        else :
            page_data.to_csv(outputfile,mode='a',index = False, header=False)

def processRemuneracionMensualPorPuesto(file,outputfile,fecha):
    pages = tabula.read_pdf(file, pages='all')
    for index, page in enumerate(pages):

        #Remove header
        page_data = page.loc[1:]
        print(index)
        # Check if it is the last page. If it is last page, remove last rows (the last rows does not hold any valuable data)
        if index == (len(pages)-1):
            maxFilas = page_data.shape[0]
            page_data = page_data[0:maxFilas-7].dropna(1)

        # Drop all the columns that does not have valid data
        page_data = page_data.dropna(axis=1)

        # Clean the data
        columns = page_data.columns
        page_data[columns[3]] = page_data[columns[3]].apply(lambda x : x.replace("\r", " "))
        page_data[columns[4]] = page_data[columns[4]].apply(lambda x : x.replace("\r", " "))
        page_data[columns[6]] = page_data[columns[6]].apply(lambda x : x.replace("\r", " "))
        page_data[columns[7]] = page_data[columns[7]].apply(lambda x : x.replace("$", "").replace(".","",x.count(".") - 1).strip())
        page_data[columns[8]] = page_data[columns[8]].apply(lambda x : x.replace("$", "").replace(".","",x.count(".") - 1).strip())
        page_data[columns[9]] = page_data[columns[9]].apply(lambda x : x.replace("$", "").strip())
        page_data[columns[10]] = page_data[columns[10]].apply(lambda x : x.replace("$", "").strip())
        page_data[columns[11]] = page_data[columns[11]].apply(lambda x : x.replace("$", "").strip())
        page_data = page_data.drop([columns[0], columns[5]], axis=1)
        page_data.insert(0, 'fecha', fecha)
        page_data = page_data.dropna();
        page_data.to_csv(outputfile,mode='a',index = False, header=False)



import os

path = './hagp'

files = []
# r=root, d=directories, f = files
filesDict = {}
for r, d, f in os.walk(path):
            if len(d):
                 #filesDict = {'2017':{},'2018':{}}
                for directory in d:
                    filesDict[directory] = {}
            for file in f:
                if '.pdf' in file:
                    #"remuneracion_mensual-FEBRERO-2020.pdf"
                    if file.startswith("remuneracion_mensual"):
                        #remuneracion_mensual-FEBRERO-2020 ->
                        # [remuneracion_mensual,FEBRERO,2020]
                        data = file.replace(".pdf","").split("-");
                        #filesDict = '2017':{},
                        yearDict = filesDict[data[2]] # solamente el diccionario 2017
                        yearDict[data[1]] = os.path.join(r, file)
print(filesDict)

for year in filesDict:
        for month in filesDict[year] :
            fecha = year+"-"+month+"-01"
            print(fecha)
            output = 'remuneracion_mensual-'+year+'.csv'
            processRemuneracionMensualPorPuesto(filesDict[year][month], output,fecha)

import tabula
pages2 = tabula.read_pdf("remuneracion_mensual-OCTUBRE-2017.pdf", pages='all')
df = pages2[0][1:]
col = df.columns
print(col)
