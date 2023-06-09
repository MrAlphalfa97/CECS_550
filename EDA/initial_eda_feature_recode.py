# -*- coding: utf-8 -*-
"""initial_EDA_feature_recode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ShqKtOg6XVWCs5YVOlfLZ_FuErwo_UQc
"""

import pandas as pd

user_log = pd.read_csv('user_log_format1[161-320].csv', iterator=True, chunksize=10000)

user_log = pd.concat(user_log, ignore_index=True)

print(user_log.head())

user_log.isnull().any()

user_log[user_log['brand_id'].isnull()]

import seaborn as sns

sns.distplot(user_log['action_type'], kde=True, hist=True)

sns.distplot(user_log['cat_id'],hist=True)

user_log['time_stamp'].astype('str')

user_log['time_str']= user_log['time_stamp'].astype('str')

user_log['Day']=user_log['time_stamp']%100

print(user_log['Day'].head())

user_log['Month']=(user_log['time_stamp']-user_log['Day'])/100

print(user_log.head())

user_log['Month']= user_log['Month'].astype('int')

print(user_log.head())

sns.distplot(user_log['Month'],hist=True)

import datetime

user_log.head()

#user_id and category
user_cat_count= user_log.groupby(['user_id','cat_id']).size()

user_cat_click_count = user_log.groupby(['user_id','cat_id','action_type']).size().to_frame()

user_cat_click_count.head()

#category action
cat_click_count = user_log.groupby(['cat_id','action_type']).size()
cat_click_count.head()

#brand action
brand_click_count = user_log.groupby(['brand_id','action_type']).size()
brand_click_count.head()

#merchandise action
mer_click_count = user_log.groupby(['item_id','action_type']).size()
mer_click_count.head()

click_activity_percent = user_log['action_type'].value_counts(normalize=True)*100

dict_user_cat = dict(zip(user_log['user_id'],user_log['cat_id']))

dict_user_brand = dict(zip(user_log['user_id'],user_log['brand_id']))

dict_user_merch = dict(zip(user_log['user_id'],user_log['item_id']))

#user category click activity
user_cat_total = user_log.groupby(['user_id','cat_id'])['action_type'].count().to_frame()
user_cat_total.head()

user_cat_total.columns = ['count total']
user_cat_total.head()

user_cat_click_count.columns = ['size']

user_cat_click_count.head()

user_cat_activity = user_cat_total.join(user_cat_click_count,how='left')
user_cat_activity['percentage'] = user_cat_activity['size']/user_cat_activity['count total']

user_cat_activity.head()

