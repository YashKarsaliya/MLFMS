# -*- coding: utf-8 -*-
"""coolingload.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OpicsYum-EhrJ0EwViYjVPKfWXjzg9eN
"""

import pandas as pd
import xgboost as xgb 
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split

data = pd.read_csv('Dataset.csv', sep=',')
data = data.drop('Unnamed: 0', axis =1)
X = data.drop(["Heating_Load","Cooling_Load"], axis=1)
y = data["Cooling_Load"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=123)

xgb_model = xgb.XGBRegressor(objective='reg:squarederror', max_depth = 8,n_estimators=1000, learning_rate=0.05)

xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(r2)
print(mae)
print(mse)

model = xgb_model

new_data = pd.read_csv('/content/Dataset_test.csv')
X_test = pd.read_csv('/content/Dataset_test.csv')
y_test = pd.read_csv('/content/Final_Value.csv')

X_test = X_test.drop('Unnamed: 0', axis=1)

y_test = y_test['Cooling_Load']

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print("r2 score:",r2,"\nMAE:",mae,"\nMSE:",mse,"\nMAPE:",mape,"\nRMSE:",rmse)

print("y_pred:",y_pred,"\ny_test:",y_test)

