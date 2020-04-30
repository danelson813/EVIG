import pandas as pd 


evig = pd.read_excel('Irrigation Group list.xlsx',
                        workbook=0,
                        index_col=0,
                        header = 4,
                        skiprows = 5)
print(evig.head())