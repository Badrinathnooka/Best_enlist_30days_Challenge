import pandas as pd
k=pd.array([1,2,3])
m=pd.datetime(2020,4,1)
print(pd._version)
print(k,m)
print()
print("BarGraph")
k=['e1','e2']
pd.set_option('display.max_rows',2)
pd.set_option('display.max_columns',2)
df=pd.read_csv('3.csv')
df.e4.value_counts().plot(kind='bar')