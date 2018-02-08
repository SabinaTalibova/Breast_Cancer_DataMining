import pandas as pd 

data=pd.read_csv('breast_cancer_dataset.csv')

#list of column names
print(data.columns.tolist())
print(data.shape)
print(data.ndim)
print(data.size)
print(data.axes)
print(data.var())