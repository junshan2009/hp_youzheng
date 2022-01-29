# !/usr/bin/env python
# -*-coding:utf-8 -*-
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from xgboost import plot_importance
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.datasets import load_iris

datasets=load_iris()
print(type(datasets.values()))
df=pd.DataFrame(datasets.values())
print(df.head())
x=datasets.data
print(x)
y=datasets.target
print(y)
# y=df['result']
# x=df[['a1','a2','a3','a4','a5','lb_en']]
# y=y.values
# x=x.values
# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.33, random_state=7)
#
# model = XGBClassifier( max_depth=9,subsample=0.5)
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# predictions = [round(value) for value in Y_pred]
# accuracy = accuracy_score(Y_test, predictions)
# precision=precision_score(Y_test, predictions,average="micro")
# print(accuracy,precision)
# print ('AUC: %.4f' % metrics.roc_auc_score(Y_test,Y_pred))
#--------------------------------特征重要性
# model.get_booster().feature_names=[['a1','a2','a3','a4','a5','lb_en'] ]
# plot_importance(model)
# plt.show()

#--------------------------另外一种特征重要性
