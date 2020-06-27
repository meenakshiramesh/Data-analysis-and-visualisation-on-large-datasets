import pandas as pd

excelfile = pd.ExcelFile('newwb .xlsx')
dframe = excelfile.parse('neww')
print(dframe)
