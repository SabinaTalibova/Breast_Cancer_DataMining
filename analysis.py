import pandas as pd 

data=pd.read_csv('data_redwine.csv')
print("list of column labes:")
print(data.columns.tolist())
print("\n")

print("dimesion of dataset:")
print(data.shape)
print("\n")

print("size of dataset:")
print(data.size)
print("\n")


print("dimesion of dataset:")
print(data.shape)
print("\n")


print("Minimum values of all attributes in dataset")
print(data.min())
print("\n")

print("Minimum value of ph column")
print(data.pH.min())
print("\n")


print("Maximum values of all attributes in dataset")
print(data.max())
print("\n")

print("Maximum value of ph column")
print(data.pH.max())
print("\n")


print("Mean values of all attributes in dataset")
print(data.mean())
print("\n")

print("Mean value of ph column")
print(data.pH.mean())
print("\n")

print("Mode values of all attributes in dataset")
print(data.mode())
print("\n")

print("Mode value of ph column")
print(data.pH.mode())
print("\n")

print("Median values of all attributes in dataset")
print(data.median())
print("\n")

print("Median value of ph column")
print(data.pH.median())
print("\n")

print("Standard deviation of all attributes in dataset")
print(data.std())
print("\n")

print("Standard deviation of ph column")
print(data.pH.std())
print("\n")

print("Variance of all attributes in dataset")
print(data.var())
print("\n")

print("Variance of ph column")
print(data.pH.var())
print("\n")

print("Correlation between ph and alcohol of wine")
print(data['pH'].corr(data['alcohol']))
print("\n")

print("Covariance between ph and alcohol of wine")
print(data['pH'].cov(data['alcohol']))
print("\n")


print("Covariance between all attributes ")
print(data.cov())
print("\n")

print("Correlation between all attributes ")
print(data.corr())
print("\n")





