#!/usr/bin/env python3
# coding:utf-8
'''

主成分分析案例
把用户进行归类。用户购买的物品类别
数据：
products.csv  商品信息
order_products__prior.csv 商品和订单信息
orders.csv 用户的订单信息
aisles.csv 商品所属具体物品类别
'''
import pandas as pd
from sklearn.decomposition import PCA

#读取四张表的数据
prior=pd.read_csv('../data/instacart/order_products__prior.csv')
products=pd.read_csv('../data/instacart/products.csv')
orders=pd.read_csv('../data/instacart/orders.csv')
aisles=pd.read_csv('../data/instacart/aisles.csv')


_pp=pd.merge(prior,products,on=["product_id","product_id"])

_po=pd.merge(_pp,orders,on=["order_id","order_id"])

_pa=pd.merge(_po,aisles,on=["aisle_id","aisle_id"])

# print(_pa.head(10))
#交叉表
cross_data=pd.crosstab(_pa['user_id'],_pa['aisle'])

print(cross_data.head(10))
print(cross_data.shape)

#进行PCA主成分分析
pca=PCA(n_components=0.9)
data=pca.fit_transform(cross_data)

print(data)
print(data.shape)