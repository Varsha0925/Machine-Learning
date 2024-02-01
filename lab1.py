import pandas as pd 
ds=pd.read_csv("iris.csv",names=["sepal_length","sepal_width","petal_length","petal_width","class"])
print(ds)
print("\n...............Sepal Length...............\n")
print("Minimum = ",ds["sepal_length"].min())
print("Maximum = ",ds["sepal_length"].max())
print("Mean = ",ds["sepal_length"].mean())
print("Standard Deviation = ",ds["sepal_length"].std())

print("\n...............Sepal Width...............\n")
print("Minimum = ",ds["sepal_width"].min())
print("Maximum = ",ds["sepal_width"].max())
print("Mean = ",ds["sepal_width"].mean())
print("Standard Deviation = ",ds["sepal_width"].std())

print("\n...............Petal length...............\n")
print("Minimum = ",ds["petal_length"].min())
print("Maximum = ",ds["petal_length"].max())
print("Mean = ",ds["petal_length"].mean())
print("Standard Deviation = ",ds["petal_length"].std())

print("\n...............Petal Width...............\n")
print("Minimum = ",ds["petal_length"].min())
print("Maximum = ",ds["petal_length"].max())
print("Mean = ",ds["petal_length"].mean())
print("Standard Deviation = ",ds["petal_length"].std())


for i in [('Iris-setosa', 'Iris-versicolor'), ('Iris-versicolor', 'Iris-virginica'), ('Iris-virginica', 'Iris-setosa')]:
    x = ds[ds["class"].isin(i)]
    correlation = x['sepal_length'].corr(x['petal_length'])
    print(f"Correlation between {i[0]} and {i[1]}: {correlation}")