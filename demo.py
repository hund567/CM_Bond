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
#数据库的全局变量
user = 'super'
password = 'Password123'
db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'

def demo():



if __name__ == '__main__':
    demo()