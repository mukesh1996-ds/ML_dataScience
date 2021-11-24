# loading all the required packages.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression, Ridge,RidgeCV, Lasso, LassoCV, ElasticNet,ElasticNetCV
import pickle

# loading the dataset.
df = pd.read_csv('Advertising.csv')
print(df.head())

# Once dataset is loaded we need to check the missing values.
print(df.isnull().sum())

# data seperation
"""x = df.drop(['Sales'], axis=1)
print(x.head())
"""
x = df.iloc[:,1:4]
print("The values of x are:",x)
y = df.Sales
print(y.head())

# After checking the null values we also need to check wheather
# multicollinearty exit or not

vif_data = pd.DataFrame()
vif_data['feature'] = x.columns
vif_data['VIF'] = [variance_inflation_factor(x.values,i)
                            for i in range(len(x.columns))]
print(vif_data)

# applying train test split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=30)

# Linear Regression
linear = LinearRegression()
linear.fit(x_train, y_train)
print(linear.intercept_)
print(linear.coef_)
new_predict = linear.predict([[ 230.1,37.8,69.2]])
print(new_predict)
# dumping the liner model into pickle file
linear_model = pickle.dump(linear, open('linear_model.pickle', 'wb'))
# Opening the pickle file and predicting the value
model = pickle.load(open('linear_model.pickle', 'rb'))
result = model.predict([[ 230.1,37.8,69.2]])
print('the resulted value is ', result.round(2))
# evaluation 
# r^2
score = linear.score(x_test,y_test)
print('the score value is:', score)

# Regularization:
# lassoCV
print('The lassoCV is used to find the best parameter for this model.')
lasso_model_cv = LassoCV(cv = 10, max_iter=2000000, normalize=True)
lasso_model_cv.fit(x_train,y_train)
print("The alpha value for this model is ",lasso_model_cv.alpha_)
print("The score value by lasso_model_cv is ",lasso_model_cv.score(x_test,y_test))
# lasso
lasso_model = Lasso(alpha=lasso_model_cv.alpha_)
lasso_model.fit(x_train, y_train)
print('the score value for lasso_model is', lasso_model.score(x_test,y_test))
# model dump:
lasso_model = pickle.dump(linear, open('lasso_model.pickle', 'wb'))

#RidgeCV
print('The RidgeCV is used to find the best parameter for this model.')
ridge_model_cv = RidgeCV(alphas= (0.1,1.0,10), cv= 10, normalize= True)
ridge_model_cv.fit(x_train,y_train)
print("The alpha value for this model is ",ridge_model_cv.alpha_)
print("The score value by ridge_model_cv is ",ridge_model_cv.score(x_test,y_test))
# lasso
ridge_model = Ridge(alpha=ridge_model_cv.alpha_)
ridge_model.fit(x_train, y_train)
print('the score value for ridge_model is', ridge_model.score(x_test,y_test))
# model dump:
ridge_model = pickle.dump(linear, open('ridge_model.pickle', 'wb'))

#ElecticnetCV
print('The ElecticnetCV is used to find the best parameter for this model.')
ElecticNet_model_cv = ElasticNetCV(alphas= None, cv= 10)
ElecticNet_model_cv.fit(x_train,y_train)
print("The alpha value for this model is ",ElecticNet_model_cv.alpha_)
print("The ratio value by ElecticNet_model_cv is ",ElecticNet_model_cv.l1_ratio_)
# ElecticNet
ElecticNet_model = ElasticNet(alpha=ElecticNet_model_cv.alpha_, l1_ratio =ElecticNet_model_cv.l1_ratio_)
ElecticNet_model.fit(x_train, y_train)
print('the score value for ElecticNet_model is', ElecticNet_model.score(x_test,y_test))
# model dump:
ElecticNet_model = pickle.dump(linear, open('ElecticNet_model.pickle', 'wb'))
