# -*- coding:utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import datetime as dt
import re
from functools import reduce
import operator
import datetime
pd.set_option('display.max_columns',None)
from sqlalchemy import create_engine
import pymysql
from WindPy import w
w.start()
from sqlalchemy.types import NVARCHAR, Float, Integer

user = 'root'
password = 'Welcome123'
db_ip = "cdb-3gsotx9q.cd.tencentcdb.com"
db_name = 'macro'
port = 10059

def get_macro():


    # 数据库创建判断
    conn = pymysql.connect(user=user, password=password, host=db_ip, charset='utf8',port=port,db=db_name)
    cur = conn.cursor()
    try:
        cur.execute("create database if not exists " + db_name + " DEFAULT CHARACTER SET utf8")
    except:
        pass



    #英文名先不做rename了 等着统一起一次就好了

    #获取所有data_type的名字
    try:
        cur.execute("select distinct data_type from dict")
    except Exception as e:
        print("Error to select,see the detail below:")
        print(e)
    data_type_list = cur.fetchall()
    for each in data_type_list:
        get_data_from_wind(each[0])
        chn_view_create(each[0])
    cur.close()
    conn.close()



def get_data_from_wind(table_name):

    engine = create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + ":" + str(port) + "/" + db_name,
                           encoding='utf-8')

    id_sql = "select id,eng_name from dict where data_type= \""+table_name+"\""
    ids = engine.execute(id_sql).fetchall()
    id_list = []
    eng_name_list = []
    for each in ids:
        id_list.append(each[0])
        eng_name_list.append(each[1])

    today = datetime.datetime.today().date()
    end_time = datetime.datetime.today().date()
    tablecheck_result = engine.execute("show tables like \"" + table_name + "\"").rowcount
    if tablecheck_result != 0:
        time_sql = "select date from " + table_name + " t order by date DESC limit 1"
        if engine.execute(time_sql).rowcount == 1:
            latest_mark_time = engine.execute(time_sql).fetchall()[0][0]
            start_time = latest_mark_time + datetime.timedelta(days=1)
        else:
            start_time = "1990-01-01"

        if latest_mark_time < today:
            winddata = w.edb(id_list, start_time, today)
            df = pd.DataFrame()
            df["date"] = winddata.Times
            df["date"] = pd.to_datetime(df['date'])

            if winddata.Times[-1] >= start_time:
                for id, singledata in zip(winddata.Codes, winddata.Data):
                    df[id] = singledata
                insert_db(df, table_name)
            else:
                print("no need to insert!")
        else:
            print("Data today has already been updated.")

    elif tablecheck_result == 0:
        start_time = "1990-01-01"
        winddata = w.edb(id_list, start_time, today)
        df = pd.DataFrame()
        df["date"] = winddata.Times
        for id, singledata in zip(winddata.Codes, winddata.Data):
            df[id] = singledata
        insert_db(df, table_name)
    else:
        print("duplicate tables exist")



def insert_db(df, table_name):

    #将dataframe以指定tablename导入sql的特定数据库中（数据库需存在，不能创建）。
    dtypedict = mapping_df_types(df)
    engine = create_engine('mysql+pymysql://'+user+":"+password+"@"+db_ip+":"+str(port)+"/"+db_name, encoding='utf-8')
    try:
        df.to_sql(table_name, con=engine, index=False, dtype=dtypedict, if_exists='append')
        print(" update successful")
    except:
        print("Error to inert,see the detail")


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



def chn_view_create(table_name):
    conn = pymysql.connect(user=user, password=password, host=db_ip,db=db_name,port=port, charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute("select column_name from information_schema.columns \
                        where table_name=\"" + table_name + "\" and data_type != \'date\'")
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

    #创建中文view
    view_sql = "create view " + table_name +"_chn  as (select date, " + \
               rename_str + " from " + table_name + ")"
    try:
        cursor.execute(view_sql)
        cursor.close()
        conn.commit()
        conn.close()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])

if __name__ == '__main__':
    get_macro()
    #视图创建
