import pandas as pd
from pandas import DataFrame

execlFile = pd.ExcelFile('Input File.xlsx')
dframe1 = execlFile.parse('one')
dframe1.to_csv('outputOne.csv', sep=',')

dframe2 = execlFile.parse('two')
dframe2.to_csv('outputTwo.csv', sep=',')

dframe3 = execlFile.parse('three')
dframe3.to_csv('outputThree.csv', sep=',')

dframe4 = execlFile.parse('four')
dframe4.to_csv('outputFour.csv', sep=',')

dframe5 = execlFile.parse('five')
dframe5.to_csv('outputFive.csv', sep=',')

dframe6 = execlFile.parse('six')
dframe6.to_csv('outputSix.csv', sep=',')

dframe7 = execlFile.parse('seven')
dframe7.to_csv('outputSeven.csv', sep=',')

dframe8 = execlFile.parse('eight')
dframe8.to_csv('outputEight.csv', sep=',')

dframe9 = execlFile.parse('nine')
dframe9.to_csv('outputNine.csv', sep=',')

dframe0 = execlFile.parse('ten')
dframe0.to_csv('outputTen.csv', sep=',')
