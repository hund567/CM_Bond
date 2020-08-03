# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from WindPy import w
w.start()
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
import datetime
def demo():
    today = datetime.datetime.today().date()
    ids = ["S0059745","S0059752"]
    winddata = w.edb(ids,"2020-07-01",today)
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + db_ip + ':3306/' + db_name, encoding='utf8')
    # pd.io.sql.to_sql(df, 'bond_name_test', conn, if_exists='append')
    # print df.index
    df = pd.DataFrame()
    df["日期"]=winddata.Times
    for id ,singledata in zip(winddata.Codes,winddata.Data):
        df[id] = singledata
    engine = create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + "/" + db_name, encoding='utf-8')

    def mapping_df_types(df):
        dtypedict = {}
        for i, j in zip(df.columns, df.dtypes):
            if "object" in str(j):
                dtypedict.update({i: NVARCHAR(length=255)})
            if "float" in str(j):
                dtypedict.update({i: Float(precision=2, asdecimal=True)})
            if "int" in str(j):
                dtypedict.update({i: Integer()})
        return dtypedict

    dtypedict = mapping_df_types(df)
    df.to_sql("国债利率", con=engine, index=False, dtype=dtypedict, if_exists='append')

    time_sql = u"select 日期 from 国债利率 order by 日期 DESC limit 1"
    start_time = engine.execute(time_sql)
    print start_time.rowcount







if __name__ == '__main__':
    demo()
