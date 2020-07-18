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


