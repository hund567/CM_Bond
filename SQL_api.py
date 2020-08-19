from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Date, Integer
import numpy as np
import pandas as pd
import pymysql

def mapping_df_types(df):
    dtypedict = {}
    for i, j in zip(df.columns, df.dtypes):
        if i=='日期':
            dtypedict.update({i: Date()})
            continue
        if "object" in str(j):
            dtypedict.update({i: NVARCHAR(length=255)})
        if "int" in str(j):
            dtypedict.update({i: Integer()})
        if "float" in str(j):
            dtypedict.update({i: Float(precision=2, asdecimal=True)})
    return dtypedict
class SQL:
    def __init__(self,host,port,db_name,user_name,password,code='utf8'):
        self.host=host
        self.port=port
        self.db=db_name
        self.user=user_name
        self.password=password
        self.code=code
        
        self.engine=create_engine('mysql+pymysql://'\
                                    +self.user+':'\
                                    +self.password+'@'\
                                    +self.host+':'\
                                    +str(self.port)+'/'\
                                    +self.db+'?'\
                                    +'charset='+self.code)

        #raise ValueError('connection failure')
    def execute(self,db,sql):
        conn=pymysql.connect(host=self.host,\
                                port=self.port,\
                                database=db,\
                                user=self.user,\
                                password=self.password,\
                                charset=self.code)
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()

    def create_database(self,db):
        sql='create database '+db
        self.execute('sys',sql)
    def drop_database(self,db):
        sql='drop database '+db
        self.execute('sys',sql)
    def upload(self,df,db,table):
        engine=create_engine('mysql+pymysql://'\
                                    +self.user+':'\
                                    +self.password+'@'\
                                    +self.host+':'\
                                    +str(self.port)+'/'\
                                    +db+'?'\
                                    +'charset='+self.code)
        dtypedict = mapping_df_types(df)
        pd.io.sql.to_sql(df,table,con = engine ,dtype=dtypedict ,if_exists = 'append',index=False)
    def read_table(self,db,sql):
        conn=pymysql.connect(host=self.host,\
                                port=self.port,\
                                database=db,\
                                user=self.user,\
                                password=self.password,\
                                charset=self.code)
        df=pd.read_sql(sql,conn)
        conn.commit()
        conn.close()
        return df
    def update_table(self,df,db,table):
        sql='drop table '+table
        self.execute(db,sql)
        self.upload(df,db,table)



#test
#mysql=SQL('mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com',3306,'sys','super','Password123')

#mysql.create_database('active_bonds_and_futures')

'''
term=['1-3Y','3-5Y','5-7Y','7-10Y','10Y+']
for i in term:
    data=pd.read_excel('1Y-各机构国债政金债同业存单净买入累计值.xlsx')
    mysql.upload(data,'lcy','1Y-各机构国债政金债同业存单净买入累计值.xlsx')
    #mysql.update_table(data,'lcy',f'{i}net_buy')
'''

'''
df=mysql.read_table('guanc','SELECT * FROM guanc.net_incr_bond where 交易类型 = \'net\' and DATE_FORMAT(日期,\'%Y-%m-%d\')>=DATE_SUB(curdate(),interval 30 day);')
print(df)
'''


