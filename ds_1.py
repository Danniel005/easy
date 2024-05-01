import pandas as pd

data = pd.read_csv("C:\\Users\\vasan\\Downloads\\iris.csv")
print("Checking complete dataset for null values\n")
print(data.isnull().to_string())
print("\n\nDescription of data in dataset\n")
print(data.describe())
print("\n\nData information such as variable names, NullType\n")
print(data.info())
print("\n\n")