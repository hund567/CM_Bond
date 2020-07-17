import pandas as pd
import os

def import_data(path, filename):
    if filename[-3:] == 'csv':
        df = pd.read_csv(path + '/' + filename, encoding = 'gbk', index_col=0)
    else:
        df = pd.read_excel(path + '/' + filename, encoding = 'gbk', index_col=0)
    date = filename[-12 : -4]
    return df, date

def df2SQL(df, date, usr, passwd, host, db_name):
    import pymysql
    conn = pymysql.connect(user = usr, password = passwd, host = host, charset = 'utf8')
    cur = conn.cursor()
    try:
        cur.execute("create database if not exists " + db_name)
    except:
        pass
    cur.execute("use " + db_name)
    try:
        sql = "create table if not exists Bonds_" + date + " (债券代码 float, 债券名称 VARCHAR(20), 待偿期 float, 开盘净价 float,\
        最高净价 float, 最低净价 float, 收盘净价 float, 加权平均净价 float, 前收盘净价 VARCHAR(10), 前加权平均净价 VARCHAR(10),\
        开盘收益率 float, 最高收益率 float, 最低收益率 float, 收盘收益率 float, 加权平均收益率 float,\
        前收盘收益率 VARCHAR(10), 前加权平均收益率 VARCHAR(10), 成交量 float, 涨跌幅 VARCHAR(10), 收益率涨跌 VARCHAR(10))"
        cur.execute(sql)
    except:
        pass
    for i in range(0, len(df)):
        record = tuple(df.iloc[i])
        try:
            sqlSentence = "insert into Bonds_" + date + " (债券代码, 债券名称, 待偿期, 开盘净价,\
            最高净价, 最低净价, 收盘净价, 加权平均净价, 前收盘净价, 前加权平均净价, 开盘收益率, 最高收益率, 最低收益率, \
            收盘收益率, 加权平均收益率, 前收盘收益率, 前加权平均收益率, 成交量, 涨跌幅, 收益率涨跌)\
            values (%s,'%s',%s,%s,%s,%s,%s,%s,'%s','%s',%s,%s,%s,%s,%s,'%s','%s',%s,'%s','%s')" % record
            cur.execute(sqlSentence)
        except:
            break
    cur.close()
    conn.commit()
    conn.close()

########## test ###########
path = r'//Users/kenkang/Documents/Python/dy/CFETS'
files = os.listdir(path)

usr = 'root'
passwd = 'eUg4N44lLiot'
host = 'localhost'
db_name = "Daily_Transaction"

df, date = import_data(path, files[1])
df2SQL(df, date, usr, passwd, host, db_name)
