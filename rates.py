# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import datetime as dt
import re
from functools import reduce
import operator
import datetime
import dateutil.parser
import os
pd.set_option('display.max_columns',None)
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
import pymysql
from WindPy import w
w.start()
from mapping import view_create
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_rate_from_wind(bond_type):
    #1.先判断表是否存在，若没有直接创建
    #2.查看表的最新更新日期，没有默认按照1990. 从wind中提取数据并直接做插入处理

    engine = create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + "/" + db_name,
                           encoding='utf-8')

    id_sql = "select id,eng_name from dict where data_type=\"bond_rate\" and name like "+"\"%%"+bond_type+"%%\""
    ids = engine.execute(id_sql).fetchall()
    id_list=[]
    eng_name_list = []
    for each in ids:
        id_list.append(each[0])
        eng_name_list.append(each[1])

    today = datetime.datetime.today().date()
    end_time = datetime.datetime.today().date()

    table_name = bond_type+"利率"
    tablecheck_result = engine.execute("show tables like \"" + table_name + "\"").rowcount
    if tablecheck_result != 0:
        time_sql = "select 日期 from "+ table_name +" t order by 日期 DESC limit 1"
        if engine.execute(time_sql).rowcount == 1:
            start_time = engine.execute(time_sql).fetchall()[0][0]
        else:
            start_time = "1990-01-01"

        winddata = w.edb(id_list, start_time, today)

        df = pd.DataFrame()
        df["日期"] = winddata.Times
        df["日期"] = pd.to_datetime(df['日期'])
        print df.dtypes
        for id, singledata in zip(winddata.Codes, winddata.Data[0]):
            df[id] = singledata
        insert_db(df,table_name)

    elif tablecheck_result == 0:
        start_time = "1990-01-01"
        winddata = w.edb(id_list, start_time, today)
        df = pd.DataFrame()
        df["日期"] = winddata.Times
        for id, singledata in zip(winddata.Codes, winddata.Data):
            df[id] = singledata
        insert_db(df, table_name)
    else:
        print "duplicate tables exist"


def insert_db(df, table_name):

    #将dataframe以指定tablename导入sql的特定数据库中（数据库需存在，不能创建）。
    dtypedict = mapping_df_types(df)
    engine = create_engine('mysql+pymysql://'+user+":"+password+"@"+db_ip+"/"+db_name, encoding='utf-8')
    try:
        df.to_sql(table_name, con=engine, index=False, dtype=dtypedict, if_exists='append')
        print " update successful"
    except:
        print "Error to inert,see the detail"


def mapping_df_types(df):
    dtypedict = {}

    for i, j in zip(df.columns, df.dtypes):
        # if "object" in str(j):
        #     dtypedict.update({i: NVARCHAR(length=255)})
        if "float" in str(j):
            dtypedict.update({i: Float(precision=2, asdecimal=True)})
        if "int" in str(j):
            dtypedict.update({i: Integer()})
    return dtypedict


if __name__ == '__main__':
    # 数据库的全局变量
    user = 'super'
    password = 'Password123'
    db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
    db_name = 'guanc'

    # 数据库创建判断
    conn = pymysql.connect(user=user, password=password, host=db_ip, charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute("create database if not exists " + db_name + " DEFAULT CHARACTER SET utf8")
    except:
        pass
    cur.close()
    conn.close()

    bond_type = ['质押式回购','同业拆借','信用拆借','互换','口行债','国债']

    get_rate_from_wind('国债')
    view_create("国债"+"利率")
