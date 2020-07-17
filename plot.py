# -*- coding:utf-8 -*-
import time
import datetime
import pymysql
from sqlalchemy import create_engine
import sys
import plotly
import plotly.graph_objects as go
import plotly.offline as py
from plotly.graph_objs import Scatter,Layout
import pandas as pd
import datetime
from sqlalchemy import create_engine
reload(sys)
sys.setdefaultencoding('utf-8')
pd.set_option('display.max_columns', None)
plotly.offline.init_notebook_mode(connected=True)

#全局变量
user = 'super'
password = 'Password123'
db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'

def get_df(faculty):

    conn = pymysql.connect(user=user, password=password, host=db_ip, db=db_name, charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute("select id from dict t1 where t1.name like \"%" + faculty + "%\"")
    except:
        pass
    ids = cursor.fetchall()
    cursor.close()
    id_str = ""
    for id in ids:
        id_str = id_str + "," + id[0]
        id_str_sum = id_str + "+" + id[0]
    id_str = id_str[1:]
    id_str_sum = id_str_sum[1:]

    sql = "select t1.bond_time," + id_str + " from original t1"
    df = pd.read_sql(sql, conn)
    df[faculty+'托管总量'] = df.iloc[:, 1:].sum(axis=1)
    df[faculty+"增量"] = ""
    df[faculty+"滚动2月增量"] = ""
    df[faculty+"滚动3月增量"] = ""
    i = 1
    while i < len(df):
        df.loc[i, faculty+"增量"] = df.loc[i, faculty+'托管总量'] - df.loc[i - 1, faculty+'托管总量']
        i = i + 1

    #滚动2个月
    i = 2
    while i < len(df):
        df.loc[i, faculty+"滚动2月增量"] = df.loc[i, faculty+'增量'] + df.loc[i - 1, faculty+'增量']
        i = i + 1

    #滚动三个月
    i = 3
    while i < len(df):
        df.loc[i, faculty+"滚动3月增量"] = df.loc[i, faculty+'增量'] + df.loc[i - 1, faculty+'增量']\
                                            + df.loc[i - 2, faculty+'增量']
        i = i + 1
    return df[['bond_time',faculty+'托管总量',faculty+'增量',faculty+'滚动2月增量',faculty+'滚动3月增量']]





if __name__ == '__main__':
    faculty = "合计"
    trade_name = "证券公司|非法人"
    df_sum = get_df(faculty)
    trade_name=trade_name.split("|")
    df_all = df_sum
    for each in trade_name:
        df_all = pd.concat([df_all,get_df(each).iloc[:,1:]], axis=1)
    #前三行有空值，删除
    df_all = df_all.drop(df_all.index[:3])

    df_all["交易盘增量"] = 0
    df_all["交易盘滚动2月增量"]  = 0
    df_all["交易盘滚动3月增量"] = 0
    df_all["交易盘托管量"] = 0

    for each in trade_name:
        df_all["交易盘增量"] = df_all["交易盘增量"] + df_all[each+"增量"]
        df_all["交易盘滚动2月增量"] = df_all["交易盘滚动2月增量"] + df_all[each+"滚动2月增量"]
        df_all["交易盘滚动3月增量"] = df_all["交易盘滚动3月增量"] + df_all[each+"滚动3月增量"]
        df_all["交易盘托管总量"] = df_all["交易盘托管量"] +  df_all[each+"托管总量"]

    df_all["交易盘增量占比"] = df_all["交易盘增量"]/df_all["合计增量"]
    df_all["交易盘滚动2月增量占比"] = df_all["交易盘滚动2月增量"]/df_all["合计滚动2月增量"]
    df_all["交易盘滚动3月增量占比"] = df_all["交易盘滚动3月增量"]/df_all["合计滚动3月增量"]

    df_all["交易盘增量占全部托管量占比"] = df_all["交易盘增量"] / df_all["合计托管总量"]





    #处理异常值
    df_all.drop( df_all[(df_all["交易盘增量占比"] > 1)|(df_all["交易盘增量占比"] < -1)].index, inplace=True )
    df_all.drop( df_all[(df_all["交易盘滚动2月增量占比"] > 1)|(df_all["交易盘滚动2月增量占比"] < -1)].index, inplace=True )
    df_all.drop( df_all[(df_all["交易盘滚动3月增量占比"] > 1)|(df_all["交易盘滚动3月增量占比"] < -1)].index, inplace=True )


    #创建benchmark
    # conn = pymysql.connect(user=user, password=password, host=db_ip, db=db_name, charset='utf8')
    # df_bench = pd.read_sql("select * from benchmark", conn)
    # conn.close()


    #作图
    trace1 = go.Scatter(
        x=df_all["bond_time"],
        y=df_all["交易盘增量占比"],
        mode = 'lines',
        name='交易盘增量占比',
    )

    trace2 = go.Scatter(
        x=df_all["bond_time"],
        y=df_all["交易盘滚动2月增量占比"],
        name='交易盘滚动2月增量占比'
                )

    trace3 = go.Scatter(
        x=df_all["bond_time"],
        y=df_all["交易盘滚动3月增量占比"],
        name='交易盘滚动3月增量占比'
        )
    trace4 = go.Scatter(
        x=df_all["bond_time"],
        y=df_all["交易盘托管全量占比"],
        name='交易盘全量/全部托管量'
    )
    trace5 = go.Scatter(
        x=df_all["bond_time"],
        y=df_all["交易盘增量占全部托管量占比"],
        name='交易盘增量/全部托管量'
    )


    data_plot = [trace1,trace2,trace3,trace4,trace5]
    layout = go.Layout(title="示例图",
                       yaxis=dict(title="交易盘(滚动)占比"),
                       legend=dict(x=0, y=1, font=dict(size=12, color="black")))
    fig = go.Figure(data=data_plot, layout=layout)
    py.plot(fig,auto_play=True)

    writer = pd.ExcelWriter('F:\my.xlsx')
    df_all.to_excel(writer, float_format='%.5f')
    writer.save()


    #更新一个plot 从2019年以后开始做
    # df_after_2019 = df_all["bond_time"]








