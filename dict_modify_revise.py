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
          "上清所":"SC",
          "交易所市场":"ExchMkt",
          "保险机构":"Insurance",
          "信用社":"CreditUnion",
          "全国性商业银行及其分支行":"NationalBank",
          "其他金融机构":"OtherFinancialIns",
          "其他银行":"OtherBanks",
           "其他":"Others",
           "其它":"Others",
           "农村合作银行":"RuralCorBank",
           "农村商业银行":"RuralBank",
           "合计":"Sum",
           "商业银行":"CommBank",
           "商业银行理财产品":"WMP",
           "城市商业银行":"CityCommBank",
           "基金公司及基金会":"MutualFund",
            "境外机构":"ForeignInst",
           "外资银行":"ForeignBank",
           "政策性银行":"PolicyBank",
           "村镇银行":"RuralBank",
           "柜台市场":"OTC",
           "自贸区市场":"FreeTradeZoneMkt",
           "证券公司":"Securities",
           "银行间债券市场":"InterBank",
           "非法人产品":"Fund",
           "非金融机构":"NonFinancialIns",
           "中国农业发展银行债":"ADB",
           "农发债":"ADB",
           "中国进出口银行债":"EXIM",
           "进出口行债":"EXIM",
           "国债":"CGB",
           "记账式国债":"CGB",
           "国家开发银行债":"SDB",
           "国开债":"SDB",
           "地方债":"LGB",
           "企业债":"EnterpriseBond",
           "商业银行二级资本债":"2TierBankBond",
           "地方政府债":"LGB",
            "中短期票据":"MTN",
           "利率互换":"IRS",
           "银行间同业拆借":"interbanklending",
           "存款类机构信用拆借":"DepositInstilending",
           "中资美元债":"USDbond",
           "商业银行同业存单":"CD",
           "商业银行普通债":"BankFinBond",
           "银行间质押式回购":"repo",
           "政府支持机构债券":"GovSponsoredInsBond ",
           "商业银行次级债":"SecondaryBankBond",
           "收盘价":"close",
           "开盘价":"open",
           "加权平均":"ma"
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
                               .replace("曲线","").replace("(","") \
                               .replace("周", "W").replace("隔夜", "OV") \

        elif "(" not in index_list[1] and ":" in index_list[1]:
            str_body = index_list[1].split(":")
            if len(str_body) >1:
                str_body = "_".join(str_body)
            else:
                str_body = str(str_body)
            str_body = str_body.replace("+", "Plus").replace("-", "Minus") \
                .replace("年", "Y").replace("月", "M") \
                .replace("天", "D").replace("个", "") \
                .replace("曲线", "").replace("(", "")\
                .replace("周", "W").replace("隔夜", "OV")
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
            .replace("天", "D").replace("个", "").replace("贷款", "Loan").replace("定存", "FD") \
            .replace("周", "W").replace("隔夜", "OV")

    eng_name = str_body.replace("__","_")
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
