from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\Kunal K.S. Sahni\\Desktop\\IET-Makeathon\\new_data.csv")
# data = data.fillna(lambda x: x.median())
data = data.fillna(method='ffill')
# np.arrange(1968728).reshape(246091,1)

X = data[['State_Name','District_Name','Crop_Year','Season','Crop','Area']]
Y = [data['Production']]

# print(X)
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.33, random_state=42)



# # print(X_train )
# #
# #
#
# X_test.fillna(X_test.mean())

# X_train.dropna()


reg = LinearRegression().fit(X_train,Y_train)
# #
#
#
#
#
# print(reg.score())
# #
# print(reg.intercept_)
# #
# print(reg.predict(X_test))
