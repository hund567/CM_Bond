# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# from WindPy import w
# w.start()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
import datetime as dt
import re
from functools import reduce
import operator
import dateutil.parser
import os
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

#这个函数就是对表头重命名
def double2Chn(name,value = 1):
    '''
    输入CFETS格式的中英混合名字（可重复），输出英文-中文字典
    '''
    uniq = pd.Series(list(set(name)))
    uniq_new = uniq.map(lambda x : (re.split('[\n]',x)[value]))
    uniq_new = uniq_new.map(lambda x : x.replace('Less then 1Y，including 1Y', '0-1Y').replace('More then 30Y',
                                            '30Y+').replace('~', '-').replace('（', '').replace('）','').replace('(',
                                             '').replace(')',''))
    uniq_new = uniq_new.map(lambda x : x.replace('基金公司及产品', '基金及产品').replace('大型商业银行/政策性银行',
                                    '大行和政策行').replace('股份制商业银行', '股份行').replace('城市商业银行',
                                    '城商行').replace('证券公司','券商').replace('理财类产品','理财').replace('短期/超短期融资券',
                                    '短融').replace('中期票据','中票').replace('资产支持证券','ABS').replace('地方政府债','地方债'))
    return dict(zip(uniq, uniq_new))


def filename2date(filename):
    # 输入带日期数字的单个文件名或者列表，输出相应日期/数字
    pattern = re.compile(r'\d{8}')

    if isinstance(filename, list):
        listofname = [pattern.findall(x) for x in filename]
        date_list = [reduce(operator.add, x) for x in listofname]
        return date_list
        # print('list')

    else:
        date = pattern.findall(filename)
        date_str = date[0]
        return date_str

def find_new_file():
    file = os.listdir("/Users/hund567/Desktop/code_pycharm/CMB_BOND")
    existing_file = pd.read_excel('existing_file_store.xlsx', index_col=0)
    existing_file.iloc[:,0].tolist()
    pd.Series(file).to_excel('existing_file_store.xlsx')

    new_file = list(set(file).difference(set(existing_file)))
    return new_file

#
def name2df_trans_bond(filename):
    '''
    输入四位月日日期，输出成交热度表
    '''
    # 将中文名称翻译为英文，形成重命名词典
    code_name_match = {'债券代码': 'code', '债券名称': 'name', '待偿期': 'maturity', '开盘净价': 'open_clean', '最高净价': 'high_clean',
                       '最低净价': 'low_clean', '收盘净价': 'close_clean', '加权平均净价': 'wa_clean', '前收盘净价': 'close_clean_last',
                       '前加权平均净价': 'wa_clean_last', '开盘收益率': 'open_yield', '最高收益率': 'high_yield', '最低收益率': 'low_yield',
                       '收盘收益率': 'close_yield', '加权平均收益率': 'wa_yield', '前收盘收益率': 'close_yield_last',
                       '前加权平均收益率': 'wa_yield_last', '成交量': 'volume', '涨跌幅': 'change_pct', '收益率涨跌': 'change_yield'}

    # 从excel中取数，重命名，将无数据的单元格设定为零
    # filename = f'现券清洗收盘行情报表_2020{month_n_date}.csv'
    data = pd.read_csv('C:\\Users\\Joyce Lin\\CFETS\\{filename}', encoding='gb2312', index_col=[0])
    data = data.rename(columns=code_name_match)
    data = data.replace('-', 0)
    data.index = [dateutil.parser.parse(filename2date(filename)).date()] * len(data)

    # 将数据单元格统一成数字格式便于运算
    for column, series in data.items():
        if series.dtype == 'object' and (column not in ['name', 'code']):
            data[column] = data[column].astype(np.float64)

    # 将看起来是数字格式的code变成string，方便后续修改
    data.code = data.code.astype(str)

    # 修改volume单位为亿，给code加上后缀ib（否则wind无法取数）
    data.volume = data.volume / 100000000
    data.code = data.code + '.IB'

    # 计算出日度收盘收益率变化（bp），并提取债券类型，将无债券类型的设定为“其他”
    data['change'] = 100 * (data.close_yield - data.close_yield_last)
    # data['bond_type'] = w.wss(list(data.code), "windl2type").Data[0]
    data['bond_type'] = "其他"
    data.bond_type.fillna(value='其他', inplace=True)

    return data


def name2df_net_incr_bond(filename):
    '''
    输入excel名称列表，输出整理完毕的dataframe供拼接
    '''
    data = pd.read_excel('/Users/hund567/Desktop/code_pycharm/CMB_BOND/data/'+filename, sheet_name=0, skiprows=4, nrows=120,
                         index_col=[0, 1], column_col=[0, 1])
    time = [dateutil.parser.parse(filename2date(filename)).date()] * len(data)

    data = data.set_index([time, data.index], drop=False)
    data.index.names = ['日期', '机构', '期限']
    data = data.replace('-', 0)

    # dic1 = double2Chn(data.index.get_level_values(0),value = 0)
    # dic2 = double2Chn(data.index.get_level_values(1))
    # dic3 = double2Chn(data.columns,value = 0)

    # dic1.update(dic2)
    # dic1.update(dic3)
    # dic = dic1

    # for column, series in data.items() :
    #    data[column] = float(data[column])

    dic = {'大型商业银行/政策性银行\n（Large Commercial Banks/Policy Banks）': '大行和政策行', '理财类产品\n（Wealth management products）': '理财',
           '其他产品类\n（else products）': '其他产品类', '城市商业银行\n（Urban Commercial Bank）': '城商行',
           '农村金融机构\n（Rural financial institutions）': '农村金融机构', '股份制商业银行\n（Joint Stock Commercial Bank）': '股份行',
           '证券公司\n（Securities companies ）': '券商', '保险公司\n（The insurance company）': '保险公司',
           '基金公司及产品\n（Fund companies and products）': '基金及产品', '境外机构\n（Foreign institutions）': '境外机构',
           '其他\n(Others)': '其他', '外资银行\n（Foreign banks）': '外资银行', '5-7年\n（5~7Y）': '5-7Y', '1-3年\n（1~3Y）': '1-3Y',
           '7-10年\n（7~10Y）': '7-10Y', '合计\n(Total)': '合计', '1年及1年以下\n（Less then 1Y，including 1Y）': '0-1Y',
           '15-20年\n（15~20Y）': '15-20Y', '20-30年\n（20~30Y）': '20-30Y', '30年以上\n（More then 30Y）': '30Y+',
           '3-5年\n（3~5Y）': '3-5Y',
           '10-15年\n（10~15Y）': '10-15Y', '政策性金融债-老债\n(Policy Financial Bond-old bond)': '政策性金融债-老债',
           '国债-老债\n（Treasury Bond-old bond）': '国债-老债', '地方政府债\n（Local Goverment Bond）': '地方债',
           '中期票据\n（Medium-term Note）': '中票', '短期/超短期融资券\n(Short-term Commercial Paper)': '短融',
           '国债-新债\n（Treasury Bond-new bond）': '国债-新债', '企业债\n（Corporate Bond）': '企业债',
           '政策性金融债-新债\n(Policy Financial Bond-new bond)': '政策性金融债-新债', '同业存单\n（CDs）': '同业存单',
           '其他\n（Others）': '其他', '资产支持证券\n（Asset-bakced Security）': 'ABS'}

    data.rename(index=dic, level=1, inplace=True)
    data.rename(index=dic, level=2, inplace=True)
    data.rename(columns=dic, inplace=True)

    data = data.replace('—', 0)

    data = data.sort_index(level=0)
    data = data.sort_index(level=1)
    data = data.sort_index(level=2)
    # 下面开始将数据写到数据库中
    engine = create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + "/" + db_name, encoding='utf-8')
    # 由于是append 我们先判断是否已经导入,如果已经导入，我们就跳过，否则执行插入
    table_name = "net_incr_bond"
    check_time = dateutil.parser.parse(filename2date(filename)).date()
    sql = "select * from " + table_name + " where 日期=\"" + str(check_time) + "\""
    check_result = engine.execute(sql).rowcount
    if check_result != 0:
        print "this data has already been inserted"
    else:
        repo_insert_db(data, table_name)


#回购
def name2df_repo(filename, dataset):
    time = dateutil.parser.parse(str(filename2date(filename))).date()
    if dataset == 1:
        data = pd.read_excel('/Users/hund567/Desktop/code_pycharm/CMB_BOND/data/'+filename, sheet_name=0, skiprows=0, nrows=6,
                             usecols=[1, 2, 3, 4, 5, 6, 7],
                             index_col=[0, 1], column_col=[0, 1, 2])
        data = data.replace('-', 0)
        data = data.reset_index(level=1)
        data = data.iloc[1:, :6]
        data.columns = ['城市商业银行', '农村金融机构', '股份制商业银行', '基金公司及产品', '其他产品类', '其他']
        data = data.set_index([[time] * 5, data.index], drop=False)

        # data = data.set_axis([['正回购方'] * 6, data.columns], axis = 1)
        data.columns.names = ['机构']

        data.index.names = ['日期', '机构']

        for column, series in data.items():
            if series.dtype == 'object':
                data[column] = data[column].astype(np.float64)


    elif dataset == 2:
        data = pd.read_excel('/Users/hund567/Desktop/code_pycharm/CMB_BOND/data/'+filename, sheet_name=0, skiprows=8, nrows=99,
                             usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index_col=[0, 1], column_col=[0])
        data = data.replace('-', 0)
        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期', '机构类型', '期限品种']
    else:
        data = pd.read_excel('/Users/hund567/Desktop/code_pycharm/CMB_BOND/data/'+filename, sheet_name=0, skiprows=110, nrows=27,
                             usecols=[0, 1, 2, 3, 4, 5], index_col=[0, 1], column_col=[0])
        data = data.replace('-', 0)
        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期','机构类型', '债券类型']
    #下面开始将数据写到数据库中
    engine = create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + "/" + db_name, encoding='utf-8')
    # 由于是append 我们先判断是否已经导入,如果已经导入，我们就跳过，否则执行插入
    table_name = "repo_" + str(dataset)
    sql = "select * from "+table_name+" where 日期=\"" + str(time)+"\""
    check_result = engine.execute(sql).rowcount
    if check_result != 0 :
        print "this data has already been inserted"
    else:
        repo_insert_db(data, table_name)

#银行间
def name2df_IB(filename, dataset):
    time = dateutil.parser.parse(filename2date(filename)).date()
    if dataset == 1:
        data = pd.read_excel('C:\\Users\\Joyce Lin\\CFETS\\{filename}', sheet_name=0, skiprows=0, nrows=6,
                             usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                             index_col=[0, 1], column_col=[0, 1, 2])

        data = data.replace('-', 0)
        data = data.reset_index(level=1)
        data = data.set_axis(data.iloc[0], axis=1)
        data = data.iloc[1:, :]

        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期', '机构']
        data.columns.names = ['']

        for column, series in data.items():
            if series.dtype == 'object':
                data[column] = data[column].astype(np.float64)

        return data

    else:
        data = pd.read_excel('C:\\Users\\Joyce Lin\\CFETS\\{filename}', skiprows=8, nrows=77, index_col=[0, 1])

        data = data.replace('-', 0)
        # match = {'期限品种':'Type', '正回购加权利率(%)':'Repo_rate', '正回购加权利率-剔除超50BP(%)':'Repo_rate_exc_abnormal',
        #        '正回购金额(百万)':'Repo_volume_in_mil', '逆回购加权利率(%)':'Reverse_Repo_rate',
        #        '逆回购加权利率-剔除超50BP(%)':'Reverse_Repo_rate_exc_abnormal', '逆回购金额(百万)':'Reverse_Repo_volume_in_mil',
        #       '净融入金额(考虑今日到期量)(百万)':'Net_cash_inflow_Repo', '正回购余额(百万)':'Repo_outstanding_in_mil',
        #         '逆回购余额(百万)':'Reverse_Repo_outstanding_in_mil',
        #        '拆入加权利率(%)':'IBborrow_rate', '拆入加权利率-剔除超50BP(%)':'IBborrow_rate_exc_abnormal', '拆入金额(百万)':'IBborrow_volume',
        #        '拆出加权利率(%)':'IBlend_rate', '拆出加权利率-剔除超50BP(%)':'IBlend_rate_exc_abnormal', '拆出金额(百万)':'IBlend_volume',
        #         '净融入金额(考虑今日到期量)(百万)':'Net_cash_inflow_IB', '拆入余额(百万)':'IBborrow_outstanding', '拆出余额(百万)':'IBlend_outstanding'}

        # data.rename(columns = match)
        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期', '机构类型', '期限品种']

        return data



def repo_insert_db(df, table_name):

    #将dataframe以指定tablename导入sql的特定数据库中（数据库需存在，不能创建）。
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

    engine = create_engine('mysql+pymysql://'+user+":"+password+"@"+db_ip+"/"+db_name, encoding='utf-8')
    try:
        df.to_sql(table_name, con=engine, index=True, dtype=dtypedict, if_exists='append')
        print "update successful"
    except:
        print "Error to inert,see the detail"



if __name__ == '__main__':
    # a =find_new_file()
    filename_list = os.listdir("/Users/hund567/Desktop/code_pycharm/CMB_BOND/data")
    for each in filename_list:
        # if "质押" in each:
        #     for i in range(1,4):
        #         print i
        #         name2df_repo(each,i)
        if "现券" in each:
            name2df_net_incr_bond(each)


