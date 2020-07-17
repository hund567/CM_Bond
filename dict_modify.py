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


#全局变量
user = 'super'
password = 'Password123'
db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'
Num_dict= {"中债":"CB",
          "上清所":"SLE",
          "交易所市场":"ExchMkt",
          "保险机构":"InsurFaculty",
          "信用社":"InsurComm",
          "全国性商业银行及其分支行":"CommerBANK",
          "其他金融机构":"other_faculty",
          "其他银行":"other_banks",
           "其他":"others",
           "其它":"others",
           "农村合作银行":"ArgCorBank",
           "农村商业银行":"ArgComBank",
           "合计":"Summary",
           "商业银行":"CommBank",
           "商业银行理财产品":"CommBankProduct",
           "城市商业银行":"CityCommBank",
           "基金公司及基金会":"Fund",
            "境外机构":"ForeignFaculty",
           "外资银行":"ForeignBank",
           "政策性银行":"PolicyBank",
           "村镇银行":"TownBank",
           "柜台市场":"OTC",
           "自贸区市场":"Free_Trade_Mkt",
           "证券公司":"Sec_Company",
           "银行间债券市场":"Inter_Bank",
           "非法人产品":"Not_Cor_Body",
           "非金融机构":"Not_Fiancial",
           "中国农业发展银行债":"ADB",
           "农发债":"ADB",
           "中国进出口银行债":"EXIM",
           "进出口行债":"EXIM",
           "国债":"CGB",
           "记账式国债":"CGB",
           "国家开发银行债":"SDB",
           "国开债":"SGB",
           "地方债":"LGB",
           "企业债":"CORB",
           "商业银行二级资本债":"CBSB",
           "地方政府债":"LGB",
            "中短期票据":"MTN",
           "利率互换":"irs",
           "银行间同业拆借":"interbanklending",
           "中资美元债":"USDbond",
           "商业银行同业存单":"CDs",
           "商业银行普通债":"BankFinBond",
           "银行间质押式回购":"repo",
           "政府支持机构债券":"GFSB",
           "商业银行次级债":"CBSB",
           "收盘价":"closingPrice",
           "开盘价":"OpeningPrice",
           "加权平均":"avg"
           }
def modify_dict():
    conn = pymysql.connect(user=user, password=password, host=db_ip, db=db_name, charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT name from dict")
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
    indexes = cursor.fetchall()
    for index in indexes:
        modify_single_index(index[0])
    cursor.close()
    conn.close()
def modify_single_index(index):
    index_ori = index
    if  "中债"  in index:
        index = index.replace("中债:","").replace("中债","")
    if "托管量" in index:
        data_type = "bond_num"
        index_list = index.split(":")
        str_head="Num"
        for each in index_list:
            if "托管量" in each:
                index_list.remove(each)
        i = 0
        while i<len(index_list):
            if str(index_list[i]) in Num_dict:
                index_list[i] = Num_dict[str(index_list[i])]
            i = i+1
        str_body = "_".join(index_list)

    elif "到期收益率" in index or "收益率曲线" in index:
        data_type = "bond_rate"
        str_head = "Rate"
        if  "到期收益率" in index:
            index_list=index.split("到期收益率")
        elif "收益率曲线" in index:
            index_list = index.split("收益率曲线")
        if str(index_list[0]) in Num_dict:
            str_body_pre = Num_dict[str(index_list[0])]
        else:
            str_body_pre = str(index_list[0])

        if "(" in index_list[1] :
            str_body = index_list[1].split("):")
            str_body = "_".join(str_body)
            str_body = str_body.replace("+","Plus").replace("-","Minus")\
                               .replace("年","Y")  .replace("月","M")\
                               .replace("天","D")  .replace("个","")\
                               .replace("曲线","").replace("(","")

        elif "(" not in index_list[1] and ":" in index_list[1]:
            str_body = index_list[1].split(":")
            if len(str_body) >1:
                str_body = "_".join(str_body)
            else:
                str_body = str(str_body)
            str_body = str_body.replace("+", "Plus").replace("-", "Minus") \
                .replace("年", "Y").replace("月", "M") \
                .replace("天", "D").replace("个", "") \
                .replace("曲线", "").replace("(", "")
        str_body = str_body_pre + "_" + str_body

    elif "加权利率" in index:
        data_type = "bond_rate"
        str_head = "Rate"
        index_list = index.split("加权利率:")
        i = 0
        while i < len(index_list):
            if str(index_list[i]) in Num_dict:
                index_list[i] = Num_dict[str(index_list[i])]
            i = i + 1
        str_body = "_".join(index_list)
        str_body = str_body.replace("+", "Plus").replace("-", "Minus") \
            .replace("年", "Y").replace("月", "M") \
            .replace("天", "D").replace("个", "") \
            .replace("曲线", "")
    else:
        data_type = "bond_rate"
        index_list = index.split(":")
        i = 0
        while i<len(index_list):
            if str(index_list[i]) in Num_dict:
                index_list[i] = Num_dict[str(index_list[i])]
            i = i+1
        str_body = "_".join(index_list)
        str_body = str_body.replace("+", "Plus").replace("-", "Minus") \
            .replace("年", "Y").replace("月", "M") \
            .replace("天", "D").replace("个", "") 

    eng_name = str_body
    #插入数据
    conn = pymysql.connect(user=user, password=password, host=db_ip, db=db_name, charset='utf8')
    cursor = conn.cursor()
    sql = "update dict set eng_name=%s ,data_type=%s where name =%s"
    val = (eng_name,data_type,index_ori)

    try:
        cursor.execute(sql,val)
        conn.commit()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
    cursor.close()
    conn.close()
if __name__ == '__main__':
    modify_dict()
