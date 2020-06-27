import pandas as pd
import seaborn as sns
from pandas import DataFrame

dframe1 = pd.read_csv('f2m_ratios.csv')
print(dframe1)

dframe2 = pd.pivot_table(dframe1,'Sex Ratio','Age','Year')
print(dframe2)

fig = sns.heatmap(dframe2).get_figure()
fig.savefig('heatmap.png')