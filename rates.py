# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# from WindPy import w
# w.start()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
import datetime as dt
import re
from functools import reduce
import operator
import dateutil.parser
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
pd.set_option('display.max_columns',None)
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
import pymysql




if __name__ == '__main__':
    # 数据库的全局变量
    user = 'super'
    password = 'Password123'
    db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
    db_name = 'guanc1'
    # 文件路径
    path_general = "C:\Users\Administrator\Desktop\data_csv\\"
    # 数据库创建判断
    conn = pymysql.connect(user=user, password=password, host=db_ip, charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute("create database if not exists " + db_name + " DEFAULT CHARACTER SET utf8")
    except:
        pass
    cur.close()
    conn.close()

    bond_type = ['质押式回购','同业拆借','信用拆借','互换','口行债','']
    modify_dict()