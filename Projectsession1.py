# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:39:17 2021

@author: Admin
"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("advertising.csv")
data.head()

fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='TV', y='Sales', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='Radio', y='Sales', ax=axs[1])
data.plot(kind='scatter', x='Newspaper', y='Sales', ax=axs[2])

# create X and y
feature_cols = ['TV']
X = data[feature_cols]
y = data.Sales

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)


print(lm.intercept_)
print(lm.coef_)

result = 6.97482 + 0.055467*50
print(result)

X_new = pd.DataFrame({'TV': [100]})
X_new.head()
lm.predict(X_new)


X_new = pd.DataFrame({'TV': [data.TV.min(), data.TV.max()]})
X_new.head()

preds = lm.predict(X_new)
preds


data.plot(kind='scatter', x='TV', y='Sales')


plt.plot(X_new, preds, c='red', linewidth=2)

import statsmodels.formula.api as smf
lm = smf.ols(formula='Sales ~ TV', data=data).fit()
lm.conf_int()


lm.pvalues

lm.rsquared


feature_cols = ['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
y = data.Sales

lm = LinearRegression()
lm.fit(X, y)

print(lm.intercept_)
print(lm.coef_)

lm = smf.ols(formula='Sales ~ TV + Radio + Newspaper', data=data).fit()
lm.conf_int()
lm.summary()

lm = smf.ols(formula='Sales ~ TV + Radio', data=data).fit()
lm.rsquared

lm = smf.ols(formula='Sales ~ TV + Radio + Newspaper', data=data).fit()
lm.rsquared


