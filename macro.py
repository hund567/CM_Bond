# -*- coding:utf-8 -*-
import pandas as pd
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
# from WindPy import w
# w.start()
from mapping import view_create
from mapping import chn_view_create

def get_macro():
    user = 'root'
    password = 'Welcome123'
    db_ip = "cdb-3gsotx9q.cd.tencentcdb.com"
    db_name = 'macro'
    port = 10059

    # 数据库创建判断
    conn = pymysql.connect(user=user, password=password, host=db_ip, charset='utf8',port=port)
    cur = conn.cursor()
    try:
        cur.execute("create database if not exists " + db_name + " DEFAULT CHARACTER SET utf8")
    except:
        pass
    cur.close()
    conn.close()






if __name__ == '__main__':
    get_macro()