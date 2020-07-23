# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
pd.set_option('display.max_columns', None)

def import_data(path, filename):
    if filename[-3:] == 'csv':
        df = pd.read_csv(path + '/' + filename, encoding = 'gbk', index_col=0)
    else:
        df = pd.read_excel(path + '/' + filename, encoding = 'utf8')
    return df

def mapping_df_types(df):
    from sqlalchemy.types import NVARCHAR, Float, DATETIME
    dtypedict = {}
    for i in df.columns:
        if df[i].values.dtype == 'object':
        #if i in cols or (df[i].values.dtype != 'float' or df[i].values.dtype != 'int'):
            dtypedict.update({i: NVARCHAR(length=255)})
        elif (df[i].values.dtype == 'float' or df[i].values.dtype == 'int'):
            dtypedict.update({i: Float})
        elif df[i].values.dtype == 'datetime64[ns]':
            dtypedict.update({i: DATETIME})
            
    return dtypedict


def data_preprocessing(file, filename):
    '''
    仅限那三个xls文件
    '''
    date = filename[-12 : -4]
    file['时间'] = date
    file['时间'] = pd.to_datetime(file['时间'], format = '%Y-%m-%d')
    if '质押' in filename or '信用拆借' in filename:
        locs = np.where(file.iloc[:, 1].isna())[0]
        df_rates = file.iloc[: locs[1],].copy()
        if '质押' in filename:
            name = ['加权利率表', '期限品种表', '机构类型表']
            df_rates.iloc[0, 1] = '逆回购方机构类型'
        else:
            name = ['加权利率表', '期限品种表']
            df_rates.iloc[0, 1] = '拆出方机构类型'
        df_rates.dropna(axis = 1, inplace = True)
        df_rates.columns = df_rates.iloc[0]
        df_rates.drop([0], inplace = True)
        df_rates.columns = [df_rates.columns[:-1], '时间']
        df_types = file.iloc[locs[1] + 1 : locs[2]].copy().reset_index(drop = True)
        df_types.columns = df_types.iloc[0]
        df_types.drop([0], inplace = True)
        df_types['机构类型'].fillna(method = 'ffill', inplace = True)
        df_types.columns = [df_types.columns[:-1], '时间']
        if '信用拆借' in filename:
            return name, [df_rates, df_types]
        else:
            df_genres = file.iloc[locs[3] + 1 :].copy().reset_index(drop = True).dropna(axis = 1, how = 'all')
            df_genres.columns = df_genres.iloc[0]
            df_genres.drop([0], inplace = True)
            df_genres['机构类型'].fillna(method = 'ffill', inplace = True)
            df_genres.dropna(inplace = True)
            df_genres.columns = [df_genres.columns[:-1], '时间']
            return name, [df_rates, df_types, df_genres]
    else:
        name = '现券市场总结表'
        print np.where(file.iloc[:, 0].isna())[0][1]
        loc = np.where(file.iloc[:, 0].isna())[0][1]
        df_market = file.iloc[loc: -1,].copy().reset_index(drop = True)
        df_market.iloc[0, 0] = '机构类型'
        df_market.columns = df_market.iloc[0]
        df_market.drop([0], inplace = True)
        df_market['机构类型'].fillna(method = 'ffill', inplace = True)
        df_market.columns = [df_market.columns[:-1], '时间']

        return name, df_market
    
    
def df2sql(usr, passwd, host, df, db_name, table_name):
    '''
    仅限那三个xls文件, 目前在思考另建一张主表并设置主键，链接现有表格的列作为外键方便索引
    '''
    from sqlalchemy import create_engine
    dtypedict = mapping_df_types(df)
    engine = create_engine('mysql+pymysql://' + usr + ':' + passwd + '@' + host + ':3306/' + db_name)
    df.to_sql(table_name, con = engine ,index = False, dtype = dtypedict, if_exists = 'replace')
    engine.dispose()
 
    
def import2sql(usr, passwd, host, lst_of_df, db_name, tb_names):
    '''
    仅限那三个xls文件
    '''
    if type(lst_of_df) == list:
        for i, j in zip(lst_of_df, tb_names):
            df2sql(usr, passwd, host, i, db_name, j)
    else:
        df2sql(usr, passwd, host, lst_of_df, db_name, tb_names)

def update2sql(usr, passwd, host, df, db_name, table_name):
    '''
    把新的数据直接放在原油表内
    '''
    from sqlalchemy import create_engine
    dtypedict = mapping_df_types(df)
    engine = create_engine('mysql+pymysql://' + usr + ':' + passwd + '@' + host + ':3306/' + db_name)
    df.to_sql(table_name, con = engine ,index = False, dtype = dtypedict, if_exists = 'append')
    engine.dispose()
    

''' 以下为测试 '''
path = r'/Users/hund567/Desktop/code_pycharm/CMB_BOND/data'
files = os.listdir(path)
usr = 'super'
password = 'Password123'
host = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'
print files[1]
df = import_data(path, files[1])
name, l = data_preprocessing(df, files[1])
import2sql(usr, passwd, host, l, db_name, name)
update2sql(usr, passwd, host, l, db_name, name)