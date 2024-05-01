import pandas as pd

data = pd.read_csv("C:\\Users\\vasan\\Downloads\\Employee_Salary.csv")
print(data.head())

df1 = data.groupby("Gender")

print("\n\nMale Statistics\n")
print(df1.get_group("Male").describe())

print("\n\nFemale Statistics\n")
print(df1.get_group("Female").describe())

d1 = pd.read_csv("C:\\Users\\vasan\\Downloads\\iris.csv")
df2 = d1.groupby("Species")

print("\n\nIris-Setosa\n")
print(df2.get_group("Setosa").describe())

print("\n\nIris-Virginica\n")
print(df2.get_group("Virginica").describe())

print("\n\nIris-Versicolor\n")
print(df2.get_group("Versicolor").describe())