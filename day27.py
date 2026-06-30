# # train test split
# from sklearn.model_selection import train_test_split
# x = [[2],[3],[4],[5],[6]] # input | features
# y = [30,40,50,60,70] # output | target
 
# # split dataset
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2 , random_state=42) # random_state
 
# print("Training features:")
# print(x_train)
 
# print("testing features:")
# print(x_test)
 
# print("training labels")
# print(y_train)
 
# print("testing labels")
# print(y_test)
 
# # linear regression
# import pandas as pd
# from sklearn.linear_model import LinearRegression
 
# data = {
#     "experience":[1,2,3,4,5],
#     "salary":[3,5,7,9,11]
# }
# df = pd.DataFrame(data)
# x = df[['experience']] # input single
# y = df['salary']
 
# model = LinearRegression()
# model.fit(x,y)
 
# # prediction
# new_data  = pd.DataFrame({
#     "experience":[6]
# })
# pred = model.predict(new_data)
# print(pred[0])

# # evaluation metrics
# import numpy as np
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score
 
# # Actual values prediction
# y_true = np.array([50,60,75,90,100])
 
# # predicted values
# y_pred = np.array([52,58,78,88,105])
 
# # mae (mean absolute error)
# mae = mean_absolute_error(y_true,y_pred)
# print(mae)
 
# # mse (mean squared error)
# mse = mean_squared_error(y_true,y_pred)
# print(mse)
 
# # rmse (square root of mse)
# rmse = np.sqrt(mse)
# print(rmse)
 
# # r2 score
# r2 = r2_score(y_true,y_pred)
# print(r2)
 

# # lasso vs ridge regression
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge,Lasso
# from sklearn.metrics import mean_absolute_error,mean_squared_error
 
# data = {
#     "size":[1000,1200,1500,1800,2000,2200,2500,2700,3000,3200],
#     "bedrooms":[2,2,3,3,3,4,4,4,5,5],
#     "age":[20,18,15,12,10,8,6,5,4,2],
#     "price":[30,35,45,50,55,60,68,72,80,85]
# }
# df = pd.DataFrame(data)
# print(df)
 
# #split data in x and y
# x = df[['size','bedrooms','age']]
# y = df['price']
 
# # split data in training and testing
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
 
# # training -> ridge regression
# ridge = Ridge(alpha=1.0)
# ridge.fit(x_train,y_train)
 
# # prediction
# ridge_p = ridge.predict(x_test)
# print("x test")
# print(x_test)
# print("prediction")
# print(ridge_p)
 
 
# # mae
# mae = mean_absolute_error(y_test,ridge_p)
# print("mae =>>>",mae)
 
# # mse
# mse =mean_squared_error(y_test,ridge_p)
# print(mse)
 
 
#  # lasso
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge,Lasso
# from sklearn.metrics import mean_absolute_error,mean_squared_error
 
# data = {
#     "size":[1000,1200,1500,1800,2000,2200,2500,2700,3000,3200],
#     "bedrooms":[2,2,3,3,3,4,4,4,5,5],
#     "age":[20,18,15,12,10,8,6,5,4,2],
#     "price":[30,35,45,50,55,60,68,72,80,85]
# }
# df = pd.DataFrame(data)
# print(df)
 
# #split data in x and y
# x = df[['size','bedrooms','age']]
# y = df['price']
 
# # split data in training and testing
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
 
# # training -> ridge regression
# lasso = Lasso(alpha=1.0)
# lasso.fit(x_train,y_train)
 
# # prediction
# lasso_p = lasso.predict(x_test)
# print("x test")
# print(x_test)
# print("prediction")
# print(lasso_p)
 
 
# # mae
# mae = mean_absolute_error(y_test,lasso_p)
# print("mae =>>>",mae)
 
# # mse
# mse = mean_squared_error(y_test,lasso_p)
# print("mse =>>>",mse)
 
# # model intercept
# print(lasso.intercept_) # 1
 
# # model coef  price = intercept + (cof1,* feat1)
# print(lasso.coef_)
 
# # logistic regression
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# data = {
#     "hours":[1,2,3,4,5,6,7],
#     "result":[0,0,0,1,1,1,1]
# }
# df = pd.DataFrame(data)
# print(df)
 
# # split x and y
# x = df[['hours']]
# y = df['result']
 
# # model
# model = LogisticRegression()
# model.fit(x,y)
 
# # prediction
# new_data = pd.DataFrame({
#     "hours":[3.4]
# })
# pred_d = model.predict(new_data)
# print(pred_d)
 
# # probability prediction
# prob_d = model.predict_proba(new_data)
# print(prob_d)
 
# knn
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
 
# #data set
# data = {
#     "weight":[100,110,120,170,180,190],
#     "fruits":[0,0,0,1,1,1] # 0 -> apple and 1 -> orange
# }
 
# df = pd.DataFrame(data)
# print(df)
 
# # split x and y
# x = df[['weight']]
# y = df['fruits']
 
# # model
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(x,y)
 
# # new data
# new_data = pd.DataFrame({
#     "weight":[1600]
# })
 
# pred_d = model.predict(new_data)
# print(pred_d)
 