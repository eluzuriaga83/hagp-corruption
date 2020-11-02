import tabula

#Read pdf into list of DataFrame
pages = tabula.read_pdf(r'D:\ICD\hagp\2020\remuneracion_mensual-ENERO-2020.pdf', pages='all')
for index, page in enumerate(pages):
    page_data = page.loc[1:]
    if index == 0 :
        page_data.to_csv(r'D:\ICD\hagp\2020\remuneracion_mensual_enero_2020.csv',mode='a',index = False, header= ['SECUENCIAL','EMPLOYEE','CARGO','Regimen laboral al que pertenece',
        'Número de partida presupuestaria',
        'Grado jerárquico o escala al que pertenece el puesto',
        'Remuneración mensual',
        'Remuneración unificada (anual)',
        'Décimo Tercera Remuneración',
        'Décima Cuarta Remuneración',
        'Horas suplementarias y extraordinarias',
        'Encargos y subrogaciones',
        'Total ingresos adicionales'])
    else :
        page_data.to_csv(r'D:\ICD\hagp\2020\remuneracion_mensual_enero_2020.csv',mode='a',index = False, header=False)
