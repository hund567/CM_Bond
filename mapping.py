# -*- coding:utf-8 -*-
import pymysql
import sys
import plotly
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')
pd.set_option('display.max_columns', None)

#全局变量
user = 'super'
password = 'Password123'
db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'

def view_create(table_name):
    conn = pymysql.connect(user=user, password=password, host=db_ip,db=db_name, charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute("select column_name from information_schema.columns \
                        where table_name=\"" + table_name + "\" and data_type != \'date'")
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
    columns = cursor.fetchall()
    columns_str = ""
    rename_str = ""
    for column in columns:
        columns_str = columns_str + "," + column[0]
        try:

            cursor.execute("select name from dict where id=\""+ column[0]+"\"")
            name = cursor.fetchall()[0][0]
            rename_str += column[0] + " \"" + name + "\","
        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            break
    rename_str = rename_str[:-1]

    #创建view
    view_sql = "create view " + table_name +"_view  as (select 日期, " + \
               rename_str + " from " + table_name + ")"
    try:
        cursor.execute(view_sql)
        cursor.close()
        conn.commit()
        conn.close()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
if __name__ == '__main__':
    view_create("国债利率")