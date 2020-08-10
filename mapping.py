# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
pd.set_option('display.max_columns', None)

#全局变量
user = 'root'
password = 'Welcome123'
db_ip = "cdb-3gsotx9q.cd.tencentcdb.com"
db_name = 'rates'
port = 10059

def view_create(table_name):
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
            cursor.execute("select eng_name from dict where id=\""+ column[0]+"\"")
            name = cursor.fetchall()[0][0]
            rename_str += column[0] + " \"" + name + "\","
        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            break
    rename_str = rename_str[:-1]

    #创建view
    view_sql = "create view " + table_name +"_eng  as (select date, " + \
               rename_str + " from " + table_name + ")"
    try:
        cursor.execute(view_sql)
        cursor.close()
        conn.commit()
        conn.close()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])

def chn_view_create(chn_table_name):
    dict_bond_type = {"质押式回购": "REPO",
                      "同业拆借": "interbanklending",
                      "信用拆借": "DepositInistlending",
                      "拆借": "IBlending",
                      "互换": "irs",
                      "口行债": "EXIM",
                      "农发债": "ADB",
                      "国债": "CGB",
                      "国开债": "SGB",
                      "地方政府债": "LGB",
                      "中短期票据": "MTN",
                      "美元债": "USDbond",
                      "企业债": "CORB",
                      "商业银行二级资本债": "CBSB",
                      "商业银行普通债": "BankFinBond",
                      "同业存单": "CDs",
                      "中资美元债": "USDbond",
                      "地方债": "LGB",
                      "农发行债": "ADB",
                      "商业银行": "CB",
                      "SHIBOR": "SHIBOR"
                      }
    table_name = dict_bond_type[chn_table_name]
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
    view_create("国债利率")