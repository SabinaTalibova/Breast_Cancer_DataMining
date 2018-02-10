import pandas as pd 
import matplotlib.pyplot as plt

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



#find correlation between quality and all other columns
columns=data.columns.tolist();
def correlationwithquality():
	for i in columns:
		correlation =data[i].corr(data['quality'])

		if correlation>0.8:
			print('there is strong correlation between  '+i +" and quality:"+ str(correlation)+"\n")
		elif correlation<0.8 and correlation>0.4:
			print('there is high correlation between  '+i +" and quality:"+ str(correlation)+"\n")
		elif correlation<0.4 and correlation>0.2:
			print('there is correlation between  '+i +" and quality:"+ str(correlation)+"\n")
		elif correlation<0.2 and correlation>0:
			print('there is not strong correlation between  '+i +" and quality:"+ str(correlation)+"\n")
		elif correlation<0.1 or correlation==0:
			print('there is not correlation between  '+i +" and quality:"+ str(correlation)+"\n")
		elif correlation==-1:

			print(i+' and quality has perfect negative correlation '+str(correlation)+ ' \n')
		else:
			print(not specified)
		

correlationwithquality()

#histogram of density
plt.hist(data['density'])
plt.show()




#scatter plot
x=data['quality']
y=data['residual sugar']

fig=plt.scatter(x, y)
plt.xlabel('Quality', fontsize=18)
plt.ylabel('residual sugar', fontsize=16)
plt.show()

#box plot
plt.boxplot(data['residual sugar'])
plt.show()

