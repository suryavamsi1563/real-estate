import numpy as np
import pandas as pd
from sklearn import linear_model

# Reading the files data from history and property files as excel sheets
history_df = pd.read_excel("regression_code/history.xlsx")
# Considering only the independent variables from the history data--Size,
# Type and Location
X = history_df.drop(['Price','Property_ID'],1)
# Considering the deepndent variables from the history data which is sold price
Y = pd.DataFrame(history_df['Price']/100000)
# Creating a linear regression model object from linear_model module
regr = linear_model.LinearRegression()
# Using the fit method to train our model with the data of history_df.Our model
# will become eligible to predict independent variables when we give the dependent
# variables
regr.fit(X,Y)


def pred_price(input_list):
    df = pd.DataFrame([input_list],columns=['Size','Type','Location'],dtype=int)
    print(df)
    guided_price = regr.predict(df)
    print(guided_price[0][0])
    return round(guided_price[0][0]*100000)