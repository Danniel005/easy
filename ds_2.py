import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\vasan\\Downloads\\Employee_Salary.csv")
print("Dataframe\n")
print(df)

print(df.isnull().to_string())

mean_exp = df["Experience"].mean()
df["Experience"].fillna(value=mean_exp,inplace=True)
df["Gender"].fillna(value="Male",inplace=True)
print("\n\nUpdated data with no missing values\n")
print(df)

print("\n\nIdentifying outliers")
print("Skewness of Experience: ",df["Experience"].skew())
print("Skewness of Salary: ",df["Salary"].skew())

df["Gender"]=df["Gender"].map({ 'Male':0, 'Female':1}).astype(float)
print("\n\nTransformed data")
print(df.head())
print(df.skew())
