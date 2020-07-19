# -*- coding:utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import time
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#全局变量
user = 'super'
password = 'Password123'
db_ip = "mysql57.rdsm05ltcjxv6y8.rds.bj.baidubce.com"
db_name = 'guanc'


def crawl_cur(type):
    #共有两套URL 一套是当前的 一套是根据时间的
    df_all = pd.DataFrame()
    url_cur = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/ibl-mth-bltn-"+type+".json"

    # para = {
    #     "year": str(y),
    #     "month": m
    # }

    header = {
        "Referer": "http://www.chinamoney.com.cn/chinese/mtmoncjgl/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http: // www.chinamoney.com.cn"
    }

    res = requests.post(url_cur, headers=header)
    if  res.status_code != 200:
        return res.content
    else:
        data = json.loads(res.content)["records"]
        for each in data:
            print each

def crawl_his():

    header = {
        "Referer": "http://www.chinamoney.com.cn/chinese/mtmoncjgl/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http: // www.chinamoney.com.cn"
    }

    #遍历时间
    year = range(2017, 2020)
    month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    for y in year:
        for m in month:
            index_types = ["tvvo","itvo","ittvo"]
            url_his = "http://www.chinamoney.com.cn/dqs/rest/dqs-u-currency/IblMthBltn"
            for index_type in index_types:
                paras = "lang=cn&empty=-1&yearMonth="+ str(y)+m +" & indexType = "+index_type
                res = requests.post(url_his,paras, headers=header)
                print res.content
                if res.status_code != 200:
                    return res.content
                else:
                    data = json.loads(res.content)["records"]
                    for each in data:
                        print each


if __name__ == '__main__':
    types = ["tran","bala","inst"]
    # for type in types:
    #     crawl_cur(type)
    crawl_his()

