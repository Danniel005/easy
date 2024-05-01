import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

boston = pd.read_csv("C:\\Users\\vasan\\Downloads\\Boston.csv")

print("<-------Dataframe Info--------->")
print(boston.info())
print("\n")

X=boston[['rm','lstat','ptratio']]
y = boston['medv']

#splitting into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


for i, feature in enumerate(X.columns):
    plt.subplot(1,3,i+1)
    plt.scatter(X[feature], y, marker='o', s=5)
    plt.title(feature)
    plt.xlabel(feature)
    plt.ylabel('MEDV')

plt.tight_layout()
plt.show()

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("<--------Visualization after fitting-------->")
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual MEDV')
plt.ylabel('Predicted MEDV')
plt.title('Actual MEDV vs Predicted MEDV')
plt.show()
print("\n")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("<------Evaluation Result----------->")
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
print('\n')
