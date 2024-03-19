import pandas as pd
url='https://raw.githubusercontent.com/akmand/datasets/main/FMLPDA_Table4_3.csv'
a=pd.read_csv(url)
print(a.head(5))
print(a.tail(5))
print(a.shape)
print(a.describe())
print(a.iloc[1:4])
print(a.loc[1:4])
b=a[a['slope']=='steep']
print(b)