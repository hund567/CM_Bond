# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import re
from functools import reduce
import operator
import dateutil.parser
import os
pd.set_option('display.max_columns',None)
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
import pymysql
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

#这个函数就是对表头重命名
def double2Chn(name,value = 1):

    uniq = pd.Series(list(set(name)))
    uniq_new = uniq.map(lambda x : (re.split('[\n]',x)[value]))
    uniq_new = uniq_new.map(lambda x : x.replace('Less then 1Y，including 1Y', '0-1Y').replace('More then 30Y',
                                            '30Y+').replace('~', '-').replace('（', '').replace('）','').replace('(',
                                             '').replace(')',''))
    uniq_new = uniq_new.map(lambda x : x.replace('基金公司及产品', '基金').replace('大型商业银行/政策性银行',
                                    '大行和政策行').replace('股份制商业银行', '股份行').replace('城市商业银行',
                                    '城商行').replace('证券公司','券商').replace('理财类产品','理财').replace('短期/超短期融资券',
                                    '短融').replace('中期票据','中票').replace('资产支持证券','ABS').replace('地方政府债','地方债')
                                    .replace('外资银行', '外资行').replace('农村金融机构','农商行').replace('保险公司','保险')
                                    .replace('基金公司及产品', '基金').replace('其他产品类', '其他产品')
                            )
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
    code_name_match = {u'债券代码': u'code', u'债券名称': u'name', u'待偿期': u'maturity', u'开盘净价': u'open_clean', u'最高净价': u'high_clean',
                       u'最低净价': u'low_clean', u'收盘净价': u'close_clean', u'加权平均净价': u'wa_clean', u'前收盘净价': u'close_clean_last',
                       u'前加权平均净价': u'wa_clean_last', u'开盘收益率': u'open_yield', u'最高收益率': u'high_yield', u'最低收益率': u'low_yield',
                       u'收盘收益率': u'close_yield', u'加权平均收益率': u'wa_yield', u'前收盘收益率': u'close_yield_last',
                       u'前加权平均收益率': u'wa_yield_last', u'成交量': u'volume', u'涨跌幅': u'change_pct', u'收益率涨跌': u'change_yield'}

    # 从excel中取数，重命名，将无数据的单元格设定为零
    # filename = f'现券清洗收盘行情报表_2020{month_n_date}.csv'
    data = pd.read_csv(path_general+filename, encoding='gb2312', index_col=[0])
    data = data.rename(columns=code_name_match)
    data = data.replace('-', 0)
    data.index = [dateutil.parser.parse(filename2date(filename)).date()] * len(data)
    data.index.name = "日期"
    time = dateutil.parser.parse(filename2date(filename)).date()
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
    # 下面开始将数据写到数据库中
    engine =  create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + ":" + str(port) + "/" + db_name,
                       encoding='utf-8')
    # 由于是append 我们先判断是否已经导入,如果已经导入，我们就跳过，否则执行插入
    table_name = "transaction_bond"
    # 检查表是否存在，若不存在直接创建表
    tablecheck_sql = "show tables like \"" + table_name + "\""
    tablecheck_result = engine.execute(tablecheck_sql).rowcount
    if tablecheck_result != 0:
        sql = "select * from " + table_name + " where 日期=\"" + str(time) + "\""
        check_result = engine.execute(sql).rowcount
        if check_result != 0:
            print(filename+",this data has already been inserted")
        else:
            insert_db(data, table_name, filename)
    elif tablecheck_result == 0:
        insert_db(data, table_name, filename)
    else:
        print("duplicate tables exist")



def name2df_net_incr_bond(filename):
    '''
    输入excel名称列表，输出整理完毕的dataframe供拼接
    '''

    xl = pd.ExcelFile(path_general+filename)
    sheet_name_list = xl.sheet_names


    for i in range(0,3):
        sheet_name = sheet_name_list[i]
        if u"机构买入" in sheet_name:
            label = "buy"
        elif u"机构卖出" in sheet_name:
            label = "sell"
        elif u"机构净买入" in sheet_name:
            label = "net"

        # 返回第一个非空行号
        data_pre = pd.read_excel(path_general + filename, sheet_name=sheet_name,nrows=120)
        data_pre = data_pre.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
        head_line_num  = data_pre.index[0]
        skiprows = 3+int(head_line_num)
        data = pd.read_excel(path_general+filename, sheet_name=sheet_name, skiprows=skiprows, nrows=120,
                             index_col=[0, 1], column_col=[0, 1])
        time = [dateutil.parser.parse(filename2date(filename)).date()] * len(data)

        data = data.set_index([time, data.index], drop=False)
        data.index.names = [u'日期', u'机构', u'期限']
        data = data.replace('-', 0)
        dic = {u'大型商业银行/政策性银行\n（Large Commercial Banks/Policy Banks）': u'大行和政策行', u'理财类产品\n（Wealth management products）': u'理财',
               u'其他产品类\n（else products）': u'其他产品', u'城市商业银行\n（Urban Commercial Bank）': u'城商行',
               u'农村金融机构\n（Rural financial institutions）': u'农商行', u'股份制商业银行\n（Joint Stock Commercial Bank）': u'股份行',
               u'证券公司\n（Securities companies ）': u'券商自营', u'保险公司\n（The insurance company）': u'保险',
               u'基金公司及产品\n（Fund companies and products）': u'基金', u'境外机构\n（Foreign institutions）': u'境外机构',
               u'其他\n(Others)': u'其他', u'外资银行\n（Foreign banks）': u'外资行', u'5-7年\n（5~7Y）': u'5-7Y', u'1-3年\n（1~3Y）': u'1-3Y',
               u'7-10年\n（7~10Y）': u'7-10Y', u'合计\n(Total)': u'合计', u'1年及1年以下\n（Less then 1Y，including 1Y）': u'0-1Y',
               u'15-20年\n（15~20Y）': u'15-20Y', u'20-30年\n（20~30Y）': u'20-30Y', u'30年以上\n（More then 30Y）': u'30Y+',
               u'3-5年\n（3~5Y）': u'3-5Y',
               u'10-15年\n（10~15Y）': u'10-15Y', u'政策性金融债-老债\n(Policy Financial Bond-old bond)': u'政策性金融债-老债',
               u'国债-老债\n（Treasury Bond-old bond）': u'国债-老债', u'地方政府债\n（Local Goverment Bond）': u'地方债',
               u'中期票据\n（Medium-term Note）': u'中票', u'短期/超短期融资券\n(Short-term Commercial Paper)': u'短融',
               u'国债-新债\n（Treasury Bond-new bond）': u'国债-新债', u'企业债\n（Corporate Bond）': u'企业债',
               u'政策性金融债-新债\n(Policy Financial Bond-new bond)': u'政策性金融债-新债', u'同业存单\n（CDs）': u'同业存单',
               u'其他\n（Others）': u'其他', u'资产支持证券\n（Asset-bakced Security）': u'ABS',
               u'国债-老债\n（Treasury Bond Off-the-Run）': u'国债-老债',u'国债-新债\n（Treasury Bond On-the-Run）': u'国债-新债',
               u'政策性金融债-新债\n(Policy Financial Bond On-the-Run)':u'政策性金融债-新债',
               u'政策性金融债-老债\n(Policy Financial Bond Off-the-Run)':u'政策性金融债-老债'

               }

        data.rename(index=dic, level=1, inplace=True)
        data.rename(index=dic, level=2, inplace=True)
        data.rename(columns=dic, inplace=True)
        data["交易类型"] = label
        data = data.replace('—', 0)
        data = data.sort_index(level=0)
        data = data.sort_index(level=1)
        data = data.sort_index(level=2)
        table_name = "net_incr_bond"
        check_time = dateutil.parser.parse(filename2date(filename)).date()
        # 检查表是否存在，若不存在直接创建表
        engine =  create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + ":" + str(port) + "/" + db_name,
                       encoding='utf-8')
        tablecheck_sql = u"show tables like \"" + table_name + "\""
        tablecheck_result = engine.execute(tablecheck_sql).rowcount
        if tablecheck_result != 0:
            sql = u"select * from " + table_name + u" where 日期=\"" + str(check_time) + u"\"" +u" and 交易类型=\"" + label + u"\""
            check_result = engine.execute(sql).rowcount
            if check_result != 0:
                print(filename+",this data has already been inserted")
            else:
                insert_db(data, table_name, filename)
        elif tablecheck_result == 0:
            insert_db(data, table_name, filename)
        else:
            print("duplicate tables exist")







#回购
def name2df_repo(filename, dataset):
    time = dateutil.parser.parse(str(filename2date(filename))).date()
    if dataset == 1:
        data = pd.read_excel(path_general+filename, sheet_name=0, skiprows=0, nrows=6,
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
        data = pd.read_excel(path_general+filename, sheet_name=0, skiprows=8, nrows=99,
                             usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index_col=[0, 1], column_col=[0])
        data = data.replace('-', 0)
        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期', '机构类型', '期限品种']
    else:
        data = pd.read_excel(path_general+filename, sheet_name=0, skiprows=110, nrows=27,
                             usecols=[0, 1, 2, 3, 4, 5], index_col=[0, 1], column_col=[0])
        data = data.replace('-', 0)
        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期','机构类型', '债券类型']
    #下面开始将数据写到数据库中
    engine =  create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + ":" + str(port) + "/" + db_name,
                       encoding='utf-8')
    # 由于是append 我们先判断是否已经导入,如果已经导入，我们就跳过，否则执行插入
    # table_name = "repo_" + str(dataset)
    # sql = "select * from "+table_name+" where 日期=\"" + str(time)+"\""
    # check_result = engine.execute(sql).rowcount
    # if check_result != 0 :
    #     print "this data has already been inserted"
    # else:
    #     insert_db(data, table_name)
    table_name = "repo_" + str(dataset)
    # 检查表是否存在，若不存在直接创建表
    tablecheck_sql = "show tables like \"" + table_name + "\""
    tablecheck_result = engine.execute(tablecheck_sql).rowcount
    if tablecheck_result != 0:
        sql = "select * from " + table_name + " where 日期=\"" + str(time) + "\""
        check_result = engine.execute(sql).rowcount
        if check_result != 0:
            print(filename+",this data has already been inserted")
        else:
            insert_db(data, table_name,filename)
    elif tablecheck_result == 0:
        insert_db(data, table_name,filename)
    else:
        print("duplicate tables exist")
#信用拆借
def name2df_IB(filename, dataset):
    time = dateutil.parser.parse(filename2date(filename)).date()
    if dataset == 1:
        data = pd.read_excel(path_general+filename, sheet_name=0, skiprows=0, nrows=6,
                             usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                             index_col=[0, 1], column_col=[0, 1, 2])

        data = data.reset_index(level=1)
        data = data.replace('-', 0)
        data.columns = data.iloc[0]
        data.drop(data.index[0], inplace=True)
        data = data.iloc[:,0:8]

        # data = data.iloc[1:, :]

        data = data.set_index([[time] * len(data), data.index], drop=False)
        data.index.names = ['日期', '机构']
        # data.columns.names = ['']

        for column, series in data.items():
            if series.dtype == 'object':
                data[column] = data[column].astype(np.float64)

    else:
        data = pd.read_excel(path_general+filename, skiprows=8, nrows=77, index_col=[0, 1])

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
    # 下面开始将数据写到数据库中
    engine =  create_engine('mysql+pymysql://' + user + ":" + password + "@" + db_ip + ":" + str(port) + "/" + db_name,
                       encoding='utf-8')
    # 由于是append 我们先判断是否已经导入,如果已经导入，我们就跳过，否则执行插入
    table_name = "IB_" + str(dataset)
    #检查表是否存在，若不存在直接创建表
    tablecheck_sql = "show tables like \""+table_name+"\""
    tablecheck_result = engine.execute(tablecheck_sql).rowcount
    if tablecheck_result != 0 :
        sql = "select * from " + table_name + " where 日期=\"" + str(time) + "\""
        check_result = engine.execute(sql).rowcount
        if check_result != 0:
            print(filename+",this data has already been inserted")
        else:
            insert_db(data, table_name, filename)
    elif tablecheck_result ==0:
        insert_db(data, table_name, filename)
    else:
        print("duplicate tables exist")


def insert_db(df, table_name,csv_name):

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

    sql_insert = 'mysql+pymysql://' + user + ":" + password + "@" + db_ip + ":" + str(port) + "/" + db_name
    engine =  create_engine(sql_insert,encoding='utf-8')
    try:
        df.to_sql(table_name, con=engine, index=True, dtype=dtypedict, if_exists='append')
        print(csv_name+" update successful")
    except Exception as e:
        print("Error to insert,see the detail below:")
        print(e)



if __name__ == '__main__':
    # 数据库的全局变量
    user = 'root'
    password = 'Welcome123'
    db_ip = "cdb-3gsotx9q.cd.tencentcdb.com"
    db_name = 'guanc'
    port = 10059
    #文件路径
    path_general = "C:\\Users\Administrator\Desktop\data_csv\\"
    # path_general = "/Users/hund567/Desktop/code_pycharm/CMB_BOND/data/"
    #数据库创建判断
    conn = pymysql.connect(user=user, password=password, host=db_ip, port=port,charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute("create database if not exists " + db_name + " DEFAULT CHARACTER SET utf8")
    except:
        pass
    cur.close()
    conn.close()

    filename_list = os.listdir(path_general)

    for each in filename_list:
        # each =  each.decode(encoding="gb2312", errors="strict")
        if u"质押" in each:
            for i in range(1,4):
                name2df_repo(each,i)
        if u"现券市场" in each:
            name2df_net_incr_bond(each)
        if u"信用拆借" in each:
            for j in range(1, 3):
                name2df_IB(each,j)
        if u"现券清洗" in each:
            name2df_trans_bond(each)





