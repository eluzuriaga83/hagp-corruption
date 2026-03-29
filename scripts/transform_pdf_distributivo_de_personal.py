import tabula

#Read pdf into list of DataFrame
pages = tabula.read_pdf(r'D:\ICD\hagp\2020\distributivo_personal-ENERO-2020.pdf', pages='all')
for index, page in enumerate(pages):
    # Remove 3 first rows from file they do not have valid data
    page_data = page.loc[3:]
    # Take only columns with data
    columns_range = page_data.columns[1:5]
    # Get final data table with correct rows and columns
    clean_page = page_data.loc[:,columns_range]
    # Get first column
    firstColumn = clean_page[clean_page.columns[0]];
    # Remove all NaN values from table
    final_page = clean_page[firstColumn.notna()].dropna()
    # If it is the first page we need to add headers
    if index == 0 :
        final_page.to_csv('distributivo_personal_enero_2020.csv',mode='a',index = False, header= ['EMPLOYEE','DEPARTMENT','EMPLOYEE','ROLE'])
    else :
        final_page.to_csv('distributivo_personal_enero_2020.csv',mode='a',index = False, header= False)
