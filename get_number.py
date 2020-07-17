# -*- coding:utf-8 -*-
import time
import datetime
import pymysql
from sqlalchemy import create_engine
import sys
# import Windpy as w
# w.start()
import pandas as pd
from sqlalchemy import create_engine
reload(sys)
sys.setdefaultencoding('utf-8')

#全局变量
user = 'super'
password = 'Password123'
db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'


def demo(start,end):

    #从字典表中取出所有字段
    conn = pymysql.connect(user=user, password=password, host=db_ip, charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute("select id from dict" )
    except:
        pass

    ids = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()

    for id in ids:
        dataframe = w.edb(id,start,end,user=True)
        conn = create_engine('mysql+pymysql://'+user+':'+password+'@'+db_ip+':3306/'+db_name, encoding='utf8')
        try:
            pd.io.sql.to_sql(dataframe,'bond_name',conn,if_exists='append')
        except:
            pass


def upadte_one():


if __name__ == '__main__':

    #待更新的表名,仍用管道符分割
    table_names = "bond_num"
    table_names = table_names.split("|")
    for table_name in table_names:


    # 获取数据库中最晚日期
    conn = pymysql.connect(user=user, password=password, host=db_ip,db=db_name, charset='utf8')
    cursor = conn.cursor()
    cursor1 = conn.cursor()
    try:
        cursor.execute("select t.time from "+ table_name +" t order by t.time DESC limit 1" )
    except:
        pass
    print cursor1.fetchall()
    #遍历时间
    start = cursor.fetchall()
    end = time.strftime("%Y-%m-%d", time.localtime())
    # delta = datetime.timedelta(months=1)
    # d = start + delta

    cursor.close()
    conn.commit()
    conn.close()
    # demo(start,end)
