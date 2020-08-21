#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#近一个月净买入情况" data-toc-modified-id="近一个月净买入情况-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>近一个月净买入情况</a></span><ul class="toc-item"><li><span><a href="#交易户近一个月国债、政金债各期限累计买入规模" data-toc-modified-id="交易户近一个月国债、政金债各期限累计买入规模-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>交易户近一个月国债、政金债各期限累计买入规模</a></span></li><li><span><a href="#配置户近一个月国债、政金债各期限累计买入规模" data-toc-modified-id="配置户近一个月国债、政金债各期限累计买入规模-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>配置户近一个月国债、政金债各期限累计买入规模</a></span></li><li><span><a href="#各机构近1个月1Y+国债、政金债净买入累计值" data-toc-modified-id="各机构近1个月1Y+国债、政金债净买入累计值-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>各机构近1个月1Y+国债、政金债净买入累计值</a></span></li><li><span><a href="#各机构近1个月1Y-国债、政金债、同业存单净买入累计值" data-toc-modified-id="各机构近1个月1Y-国债、政金债、同业存单净买入累计值-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>各机构近1个月1Y-国债、政金债、同业存单净买入累计值</a></span></li></ul></li><li><span><a href="#周度历史序列：分券种、期限净增持规模" data-toc-modified-id="周度历史序列：分券种、期限净增持规模-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>周度历史序列：分券种、期限净增持规模</a></span><ul class="toc-item"><li><span><a href="#各机构分券种净增持规模" data-toc-modified-id="各机构分券种净增持规模-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>各机构分券种净增持规模</a></span></li><li><span><a href="#基金全券种各期限净增持规模" data-toc-modified-id="基金全券种各期限净增持规模-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>基金全券种各期限净增持规模</a></span></li><li><span><a href="#基金利率债各期限净增持规模" data-toc-modified-id="基金利率债各期限净增持规模-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>基金利率债各期限净增持规模</a></span></li><li><span><a href="#基金各券种全部期限净增持规模" data-toc-modified-id="基金各券种全部期限净增持规模-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>基金各券种全部期限净增持规模</a></span></li><li><span><a href="#境外机构和外资行各期限净增持规模" data-toc-modified-id="境外机构和外资行各期限净增持规模-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>境外机构和外资行各期限净增持规模</a></span></li><li><span><a href="#境外机构和外资行分券种净增持规模" data-toc-modified-id="境外机构和外资行分券种净增持规模-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>境外机构和外资行分券种净增持规模</a></span></li><li><span><a href="#理财产品各期限净增持规模" data-toc-modified-id="理财产品各期限净增持规模-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>理财产品各期限净增持规模</a></span></li><li><span><a href="#理财产品各券种全部期限净增持规模" data-toc-modified-id="理财产品各券种全部期限净增持规模-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>理财产品各券种全部期限净增持规模</a></span></li><li><span><a href="#券商全券种各期限净增持规模" data-toc-modified-id="券商全券种各期限净增持规模-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>券商全券种各期限净增持规模</a></span></li><li><span><a href="#券商利率债各期限净增持规模" data-toc-modified-id="券商利率债各期限净增持规模-2.10"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>券商利率债各期限净增持规模</a></span></li><li><span><a href="#券商各券种全部期限净增持规模" data-toc-modified-id="券商各券种全部期限净增持规模-2.11"><span class="toc-item-num">2.11&nbsp;&nbsp;</span>券商各券种全部期限净增持规模</a></span></li></ul></li><li><span><a href="#利率债及存单最新日度净买入量" data-toc-modified-id="利率债及存单最新日度净买入量-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>利率债及存单最新日度净买入量</a></span><ul class="toc-item"><li><span><a href="#各机构分期限利率债日度净买入量（1Y+）" data-toc-modified-id="各机构分期限利率债日度净买入量（1Y+）-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>各机构分期限利率债日度净买入量（1Y+）</a></span></li><li><span><a href="#各机构分期限利率债+同业存单日度净买入量（1Y-）" data-toc-modified-id="各机构分期限利率债+同业存单日度净买入量（1Y-）-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>各机构分期限利率债+同业存单日度净买入量（1Y-）</a></span></li></ul></li></ul></div>

# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import datetime as dt
from math import *
from SQL_api import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import IPython.core.display as di



css_str='''

<div class="cell border-box-sizing code_cell rendered">

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">

        <style>
        @font-face {
          font-family: 'iconfont';  /* project id 1446715 */
          src: url('https://at.alicdn.com/t/font_1446715_7xyxjj2uxaq.eot');
          src: url('https://at.alicdn.com/t/font_1446715_7xyxjj2uxaq.eot?#iefix') format('embedded-opentype'),
          url('https://at.alicdn.com/t/font_1446715_7xyxjj2uxaq.woff2') format('woff2'),
          url('https://at.alicdn.com/t/font_1446715_7xyxjj2uxaq.woff') format('woff'),
          url('https://at.alicdn.com/t/font_1446715_7xyxjj2uxaq.ttf') format('truetype'),
          url('https://at.alicdn.com/t/font_1446715_7xyxjj2uxaq.svg#iconfont') format('svg');
        }
        .iconfont{
            font-family:"iconfont" !important;
            font-size:16px;font-style:normal;
            -webkit-font-smoothing: antialiased;
            -webkit-text-stroke-width: 0.2px;
            -moz-osx-font-smoothing: grayscale;
        }
        #notebook-container>.border-box-sizing:first-child{
            position:fixed;
            left:0px;
            background:#fff;
            border:0px;
            border-right:1px solid #eee;
            top:0px;
            font-size:0.8em;
            z-index:9999;
            width:320px;
            height:100%;
        }
        #notebook-container>.border-box-sizing:first-child h1{
            margin-top:0px;
        }
        #notebook-container>.border-box-sizing:first-child .rendered_html{
            overflow-y: hidden; 
            margin-right:5px;
            height:100%;
        }
        #notebook-container>.border-box-sizing:first-child .toc{
             overflow-y: auto; 
             -webkit-overflow-scrolling: touch;
             height: calc(100% - 60px);
             z-index: 99999;
        }
        #notebook-container>.border-box-sizing:first-child ul{
            padding-left:1.2em;
            list-style:none;
        }
        #notebook-container>.border-box-sizing:first-child .toc>.toc-item{
            padding-left:0em;
        }
        .border-box-sizing .container{
             width:calc(100% - 300px) !important;
             float:right;
        }
        #catalogSearchInput{
            margin:5px 0px 0px 0px;
            width:100%;
        }
        .resize-bar{
            cursor: e-resize;
            width: 16px;
            height: 16px;
            top: calc(50% - 8px);
            right: -3px;
            position:absolute;
        }
        .catalog-fa{
            float:right;
            margin-right: 15px;
            margin-top: 10px;
            font-size:36px;
            color:red;
            cursor:pointer;
        }
        .catalog-icon-container{
            position:absolute;
            z-index: 99999;
            width: 100%;
            height: 30px;
        }
        .catalog-collapse-fa{
            position:fixed;
            top:5px;
            left:5px;
            font-size:36px;
            color:red;
            cursor:pointer;
        }
        .collapse-catalog-icon-container{
            position:relative;
            z-index: 99999;
        }
        </style>
        <script>
            function resizeContainer(){
                var leftWidth = $("#notebook-container>.border-box-sizing:first-child").width();
                if($("#notebook-container>.border-box-sizing:first-child").is(":hidden")) {
                    leftWidth = 25
                }
                $("#notebook .container").css("cssText", "width:calc(100% - " + leftWidth + "px) !important");
                window.dispatchEvent(new Event('resize'));
            }
            function collapseCatalog(){
                $("#notebook-container>.border-box-sizing:first-child").show();
                $('.collapse-catalog-icon-container').remove()
                resizeContainer();
                alertMsg()
            }
            function shrinkCatalog(first){
                $("#notebook-container>.border-box-sizing:first-child").hide();
                $("body").append("<div class='collapse-catalog-icon-container'><i class='iconfont catalog-collapse-fa' onclick='collapseCatalog()'>&#xe6cc;</i></div>")
                resizeContainer();
                if(!first){
                    alertMsg()
                }
            }
            <!-- 搜索框 -->
            $("#notebook-container>.border-box-sizing:first-child h1").after("<input id='catalogSearchInput' placeholder='搜索...' />")
            $("#catalogSearchInput").bind("input propertychange",function(event){
               var val = $(this).val();
               if(val == '') {
                   $("#notebook-container>.border-box-sizing:first-child .toc li").show()
               }else{
                   $("#notebook-container>.border-box-sizing:first-child .toc li").each(function(){
                       if($(this).find("a").text().indexOf(val) != -1) {
                           $(this).show();
                       }else{
                           $(this).hide();
                       }
                   })
               }
            });
            <!-- resize bar -->
            $("#notebook-container>.border-box-sizing:first-child .toc").after("<div class='resize-bar' id='catalogResizeBtn'><i class='iconfont'>&#xe691;</i></div>");
            $("#catalogResizeBtn").mousedown(function(beigin){
                var beiginX = beigin.clientX;
                var beiginWidth = $("#notebook-container>.border-box-sizing:first-child").width();
                $(document).mousemove(function(to){
                    var toX = to.clientX;
                    var gap = toX - beiginX;
                    var adjustWidth = beiginWidth + gap
                    $("#notebook-container>.border-box-sizing:first-child").width(adjustWidth);
                    resizeContainer();
                    return false;
                })
                $(document).mouseup(function(){
                    $(document).unbind('mousemove');
                    $(document).unbind('mouseup');
                    return false;
                })
                return false;
            })
            if($("body.notebook_app").length == 0) {
                $("#notebook-container>.border-box-sizing:first-child").append("<div class='catalog-icon-container'><i class='iconfont catalog-fa' onclick='shrinkCatalog()'>&#xe6cb;</i></div>");
            }
            //resizeContainer();
            //collapse();
            if(navigator.userAgent.match(/mobile/i)) {
                //手机端默认隐藏显示滑块
                shrinkCatalog(true);
                $("#notebook-container>.border-box-sizing:first-child").css('width','220px');
                $("#notebook-container>.border-box-sizing:first-child .rendered_html").css({'margin-right':'0'});
                $("#catalogResizeBtn").hide();
            }
        </script>
    
</div>

</div>

</div>
</div>

</div>
'''


# In[3]:


di.HTML(css_str)


# In[4]:


di.display_html('<script>jQuery(function() {if(jQuery("body.notebook_app").length==0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>',raw=True)


# In[5]:



#根据净值计算累计值，结果仅保留累计值
def accumulate(df,participants,types,combine,everytype):
    datelist=sorted(list(set(df['日期'].tolist())))
    for part in participants:
        for i in range(len(df)):
            if everytype:
                for _type in types:
                    df.loc[i,f'{part}{_type}净买入累计值']=df.loc[:i,f'{part}{_type}净买入'].sum()
            else:
                df.loc[i,f'{part}净买入累计值']=df.loc[:i,f'{part}净买入'].sum()
    
    if combine==True:
        if everytype:
            for _type in types:
                df[f'境外机构和外资行{_type}净买入累计值']=df[[f'境外机构{_type}净买入累计值',f'外资行{_type}净买入累计值']].apply(lambda x: x.sum(),axis=1)
                df=df.drop([f'境外机构{_type}净买入累计值',f'外资行{_type}净买入累计值'],axis=1)
        else:        
            df['境外机构和外资行净买入累计值']=df[['境外机构净买入累计值','外资行净买入累计值']].apply(lambda x: x.sum(),axis=1)
            df=df.drop(['境外机构净买入累计值','外资行净买入累计值'],axis=1)

    columns=[]
    for part in participants:
        if everytype:
            for _type in types:
                columns.append(f'{part}{_type}净买入')
        else:
            columns.append(f'{part}净买入')
    df=df.drop(columns,axis=1)

    return df
#根据净值计算周度累计值，结果仅保留累计值
def weekly_accumulate(df,participants,types,combine,everytype):
    df['日期']=pd.to_datetime(df['日期'])
    weekly_data=df.resample('w',on='日期').sum()
    for part in participants:
        if everytype:
            for _type in types:
                weekly_data=weekly_data.rename(columns={f'{part}{_type}净买入累计值':f'{part}{_type}周度净买入累计值'})
        else:
            weekly_data=weekly_data.rename(columns={f'{part}净买入累计值':f'{part}周度净买入累计值'})
    
    if combine==True:
        if everytype:
            for _type in types:
                weekly_data[f'境外机构和外资行{_type}周度净买入累计值']=weekly_data[[f'境外机构{_type}周度净买入累计值',f'外资行{_type}周度净买入累计值']].apply(lambda x: x.sum(),axis=1)
                weekly_data=weekly_data.drop([f'境外机构{_type}周度净买入累计值',f'外资行{_type}周度净买入累计值'],axis=1)
        else:
            weekly_data['境外机构和外资行周度净买入累计值']=weekly_data[['境外机构周度净买入累计值','外资行周度净买入累计值']].apply(lambda x: x.sum(),axis=1)
            weekly_data=weekly_data.drop(['境外机构周度净买入累计值','外资行周度净买入累计值'],axis=1)
    
    columns=[]
    for part in participants:
        if everytype:
            for _type in types:
                columns.append(f'{part}{_type}净买入')
        else:
            columns.append(f'{part}净买入')
    weekly_data=weekly_data.drop(columns,axis=1)

    weekly_data=weekly_data.reset_index()
    return weekly_data

#全局变量
std_terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+','合计']
#对于非标准期限，进行换算，输入以给定节点为首尾的字符串，返回两个期限之间的所有标准期限，例如输入'7-20Y'，返回['7-10Y','10-15Y','15-20Y']
def term_analyse(term,std_terms):
    std=std_terms[:]
    std.pop(-1)
    result=[]
    if term[-1]=='+':
        term=term[:-2]
        for i in ['30','20','15','10','7','5','3','1']:
            result.append(std.pop())
            if term ==i:
                return result

    elif term[-1]=='-':
        term=term[:-2]
        for i in ['1','3','5','7','10','15','20','30']:
            result.append(std.pop(0))
            if term ==i:
                return result
    else:
        head,rear=term[:-1].split('-')
        for i in ['1','3','5','7','10','15','20','30']:
            span=std.pop(0)
            if int(head)<int(i) and int(i)<=int(rear):
                result.append(span)

        return result

def append_rates(df,weekly,datelist):

    user='root'
    password='Welcome123'
    db_ip='cdb-3gsotx9q.cd.tencentcdb.com'
    db_name='guanc'
    port=10059
    mysql=SQL(db_ip,port,'sys',user,password)
    #从sql导出收益率数据
    db_name='rates'
    table_name='SDB_eng'
    start=str(datelist[0]-dt.timedelta(days=1))
    #start=str(datelist[0])
    end=str(datelist[-1])
    sql=f'SELECT date, SDB_10Y FROM {db_name}.{table_name} where DATE_FORMAT(date,\'%Y-%m-%d\') between \'{start}\' and \'{end}\';'
    rates=mysql.read_table(db_name,sql)
    rates['date']=pd.to_datetime(rates['date'])
    #如果要设定初值，把上面start换为str(datelist[0]),再加上下面的四行代码即可
    #初值记为0
    initial=0
    time0=pd.to_datetime(datelist[0]-dt.timedelta(days=1),format='%Y-%m-%d')
    rate_dic=pd.DataFrame({'date':[time0],'SDB_10Y':[np.nan]})
    rates=pd.concat([rate_dic,rates],axis=0,ignore_index=True)
    if weekly:
        weekly_rates=rates.resample('w',on='date').mean()
        weekly_rates=weekly_rates.reset_index()
        weekly_rates=weekly_rates.rename({'date':'日期'})
        df=pd.concat([df,weekly_rates['SDB_10Y']],axis=1)
    else:
        rates=rates.rename({'date':'日期'})
        df=pd.concat([df,rates['SDB_10Y']],axis=1)

    return df


def net_buy(origin,datelist,paras,data):
    
    global std_terms

    participants,terms,types,weekly,everyterm,everytype=paras[data]
    df_dic={}
    
    columns=['日期','机构','期限']+types[:]
    origin=origin.loc[(origin['机构'].isin(participants))][columns]
    for term in terms:

        #生成空表,如果需要分券种的则券种各一列
        result_dic={'日期':[]}
        for part in participants:
            if everytype:
                for _type in types:
                    result_dic[f'{part}{_type}净买入']=[]
                    result_dic[f'{part}{_type}净买入累计值']=[]                    
            else:
                result_dic[f'{part}净买入']=[]
                result_dic[f'{part}净买入累计值']=[]
        result=pd.DataFrame(result_dic)
        
        #初值全为0
        timedelta=dt.timedelta(days=1)
        time0=pd.to_datetime(datelist[0]-timedelta,format='%Y-%m-%d')
        day_dic={'日期':time0}
        for part in participants:
            if everytype:
                for _type in types:
                    day_dic[f'{part}{_type}净买入']=0
                    day_dic[f'{part}{_type}净买入累计值']=0
            else:
                day_dic[f'{part}净买入']=0
                day_dic[f'{part}净买入累计值']=0
        result=result.append(day_dic,ignore_index=True)


        for day in datelist:
            day_dic={'日期':day}

            for part in participants:
                if everytype:
                    for _type in types:
                        if term in std_terms:
                            net=origin.loc[(origin['日期']==day) & (origin['机构']==part) & (origin['期限']==term)][_type]
                            day_dic[f'{part}{_type}净买入']=0 if len(net)==0 else round(net.values[0])
                            day_dic[f'{part}{_type}净买入累计值']=0 if len(net)==0 else round(net.values[0])
                        else:
                            termlist=term_analyse(term,std_terms)
                            net=origin.loc[(origin['日期']==day) & (origin['机构']==part) & (origin['期限'].isin(termlist))][_type]
                            day_dic[f'{part}{_type}净买入']=round(net.sum())
                            day_dic[f'{part}{_type}净买入累计值']=round(net.sum())
                else:
                    if term in std_terms:
                        net=origin.loc[(origin['日期']==day) & (origin['机构']==part) & (origin['期限']==term)][types].apply(lambda x: x.sum(),axis=1)
                        day_dic[f'{part}净买入']=0 if len(net)==0 else round(net.values[0])
                        day_dic[f'{part}净买入累计值']=0 if len(net)==0 else round(net.values[0])
                    else:
                        termlist=term_analyse(term,std_terms)
                        net=origin.loc[(origin['日期']==day) & (origin['机构']==part) & (origin['期限'].isin(termlist))][types].apply(lambda x: x.sum(),axis=1)                   
                        day_dic[f'{part}净买入']=round(net.sum())
                        day_dic[f'{part}净买入累计值']=round(net.sum())                  

            result=result.append(day_dic,ignore_index=True)

        #计算累计值
        combine=True if ('境外机构' in participants and '外资行' in participants) else False
        result=accumulate(result,participants,types,combine,everytype) if weekly==False else weekly_accumulate(result,participants,types,combine,everytype)

        #返回值为字典，key为期限
        df_dic[term]=result


    #若需要合计各期限，则将不同期限制成同一张表
    if everyterm==True:
        df=pd.DataFrame()
        for term in df_dic.keys():
            for column in df_dic[term].columns:
                if column=='日期' and len(df)==0:
                    df=pd.concat([df,df_dic[term][column]],axis=1)
                elif column !='日期':
                    df_dic[term]=df_dic[term].rename(columns={column:f'{term}{column}'})
                    df=pd.concat([df,df_dic[term][f'{term}{column}']],axis=1) 
        return df
    else:
        return df_dic

def cs_net_buy(origin,paras,data):

    global std_terms

    participants,terms,types,weekly,everyterm,everytype=paras[data]
    df_dic={}

    columns=['日期','机构','期限']+types[:]
    origin=origin.loc[(origin['机构'].isin(participants))][columns]
    term_dic={}
    for term in terms:
        result_dic={}

        if term in std_terms:
            df=origin.loc[origin['期限']==term]
            result_dic['机构']=df['机构'].values
            for _type in types:
                result_dic[_type]=df[_type].values
            result_dic['合计']=origin.loc[origin['期限']==term][types].apply(lambda x: x.sum(),axis=1).values

        else:
            termlist=term_analyse(term,std_terms)
            result_dic['机构']=participants
            for _type in types:
                result_dic[_type]=[]
            result_dic['合计']=[]
            for part in participants:
                for _type in types:
                    type_data=origin.loc[(origin['机构']==part)&(origin['期限'].isin(termlist))][_type].values
                    result_dic[_type].append(type_data.sum())
                sum_data=origin.loc[(origin['机构']==part)&(origin['期限'].isin(termlist))][types].apply(lambda x: x.sum(),axis=1)
                result_dic['合计'].append(sum_data.sum())

        result=pd.DataFrame(result_dic)
        term_dic[term]=result


    return term_dic
#####################################参数设置#####################################

paras={}
######图一######
#参与者设置
participants=['基金','券商自营']
#期限设置
terms=['1-3Y','3-5Y','5-7Y','7-10Y','10Y+']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债']
#是否周度数据
weekly=False
everyterm=False
everytype=False
paras['data1']=[participants,terms,types,weekly,everyterm,everytype]

######图二######
#参与者设置
participants=['理财','境外机构','外资行','保险','大行和政策行','股份行','农商行']
#期限设置
terms=['1-3Y','3-5Y','5-7Y','7-10Y','10Y+']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债']
#是否周度数据
weekly=False
everyterm=False
everytype=False
paras['data2']=[participants,terms,types,weekly,everyterm,everytype]

######图三、四######
#参与者设置
participants1=['城商行','理财','境外机构','外资行','保险','大行和政策行','股份行','农商行','其他产品类','其他']
participants2=['基金','券商自营']
#期限设置
terms=['1Y+']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债']
#是否周度数据
weekly=False
everyterm=False
everytype=False
paras['data3配置']=[participants1,terms,types,weekly,everyterm,everytype]
paras['data3交易']=[participants2,terms,types,weekly,everyterm,everytype]


######图五、(六)######
#参与者设置
participants1=['城商行','理财','境外机构','外资行','保险','大行和政策行','股份行','农商行','其他产品','其他']
participants2=['基金','券商自营']
#期限设置
terms=['1Y-']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债','同业存单']
weekly=False
everyterm=False
everytype=False
paras['data4配置']=[participants1,terms,types,weekly,everyterm,everytype]
paras['data4交易']=[participants2,terms,types,weekly,everyterm,everytype]

######图六 周度数据######
#参与者设置
participants=['城商行','基金','券商自营','理财','境外机构','外资行','保险','大行和政策行','股份行','农商行','其他产品','其他']
#期限设置
terms=['合计']
#券种设置
types=['合计']
weekly=True
everyterm=False
everytype=False
paras['data6']=[participants,terms,types,weekly,everyterm,everytype]

######图七######
#参与者设置
participants=['基金']
#期限设置
terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+']
#券种设置
types=['合计']
weekly=True
everyterm=True
everytype=False
paras['data7']=[participants,terms,types,weekly,everyterm,everytype]

######图八######
#参与者设置
participants=['基金']
#期限设置
terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债']
weekly=True
everyterm=True
everytype=False
paras['data8']=[participants,terms,types,weekly,everyterm,everytype]

######图九######
#参与者设置
participants=['基金']
#期限设置
terms=['合计']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债','中票','短融','企业债','地方债','同业存单','ABS','其他']
weekly=True
everyterm=False
everytype=True
paras['data9']=[participants,terms,types,weekly,everyterm,everytype]

######图十######
#参与者设置
participants=['境外机构','外资行']
#期限设置
terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+']
#券种设置
types=['合计']
weekly=True
everyterm=True
everytype=False
paras['data10']=[participants,terms,types,weekly,everyterm,everytype]

######图十一######
#参与者设置
participants=['境外机构','外资行']
#期限设置
terms=['合计']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债','中票','短融','企业债','地方债','同业存单','ABS','其他']
weekly=True
everyterm=False
everytype=True
paras['data11']=[participants,terms,types,weekly,everyterm,everytype]

######图十二######
#参与者设置
participants=['理财']
#期限设置
terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+']
#券种设置
types=['合计']
weekly=True
everyterm=True
everytype=False
paras['data12']=[participants,terms,types,weekly,everyterm,everytype]

######图十三######
#参与者设置
participants=['理财']
#期限设置
terms=['合计']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债','中票','短融','企业债','地方债','同业存单','ABS','其他']
weekly=True
everyterm=False
everytype=True
paras['data13']=[participants,terms,types,weekly,everyterm,everytype]

######图十四######
#参与者设置
participants=['券商自营']
#期限设置
terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+']
#券种设置
types=['合计']
weekly=True
everyterm=True
everytype=False
paras['data14']=[participants,terms,types,weekly,everyterm,everytype]

######图十五######
#参与者设置
participants=['券商自营']
#期限设置
terms=['0-1Y','1-3Y','3-5Y','5-7Y','7-10Y','10-15Y','15-20Y','20-30Y','30Y+']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债']
weekly=True
everyterm=True
everytype=False
paras['data15']=[participants,terms,types,weekly,everyterm,everytype]

######图十六######
#参与者设置
participants=['券商自营']
#期限设置
terms=['合计']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债','中票','短融','企业债','地方债','同业存单','ABS','其他']
weekly=True
everyterm=False
everytype=True
paras['data16']=[participants,terms,types,weekly,everyterm,everytype]

######图十七######
#参与者设置
participants=['城商行','基金','券商自营','理财','境外机构','外资行','保险','大行和政策行','股份行','农商行','其他产品','其他']
#期限设置
terms=['1-3Y','3-5Y','5-7Y','7-10Y','10Y+']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债']
weekly=False
everyterm=False
everytype=True
paras['data17']=[participants,terms,types,weekly,everyterm,everytype]

######图十八######
#参与者设置
participants=['城商行','基金','券商自营','理财','境外机构','外资行','保险','大行和政策行','股份行','农商行','其他产品','其他']
#期限设置
terms=['0-1Y']
#券种设置
types=['国债-新债','国债-老债','政策性金融债-新债','政策性金融债-老债','同业存单']
weekly=False
everyterm=False
everytype=True
paras['data18']=[participants,terms,types,weekly,everyterm,everytype]
#####################################run#####################################

#直接从sql导入
user='root'
password='Welcome123'
db_ip='cdb-3gsotx9q.cd.tencentcdb.com'
db_name='guanc'
port=10059
mysql=SQL(db_ip,port,'sys',user,password)
db_name='guanc'
table_name='net_incr_bond'
#图1-5
timedelta=30
sql=f'SELECT * FROM {db_name}.{table_name} where 交易类型 = \'net\' and DATE_FORMAT(日期,\'%Y-%m-%d\')>=DATE_SUB(curdate(),interval {timedelta} day);'
#图6-13
#sql=f'SELECT * FROM {db_name}.{table_name} where 交易类型 = \'net\' ;'

origin=mysql.read_table('guanc',sql)


#获取日期序列
datelist=sorted(list(set(origin['日期'].tolist())))



#net_buy函数范围一个字典，value为dataframe，key值为对应期限


# In[6]:


titles_dic = {'data1':'交易户：','data2':'配置户：','data3交易':'交易户：','data3配置':'配置户：','data4交易':'交易户：','data4配置':'配置户：',
             'data6':'各主要机构','data7':'基金全部券种','data8':'基金利率债','data9':'基金','data10':'境外机构和外资行','data11':'境外机构和外资行',
              'data12':'理财','data13':'理财','data14':'券商全部券种','data15':'券商利率债','data16':'券商'}
legend_dic = {'data6':'','data7':'基金','data8':'基金','data9':'基金','data10':'境外机构和外资行','data11':'境外机构和外资行',
              'data12':'理财','data13':'理财','data14':'券商自营','data15':'券商自营','data16':'券商自营'}


def line_net(data):
    dic=net_buy(origin,datelist,paras,data)
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    
    # 对每个期限作图
    for term in terms:
        df = append_rates(dic[term],weekly,datelist)
        lst = []
        names = list(df.columns)
        for i in range(len(names)-1):
            names[i]=names[i][0:-6] # 图例中去掉"净买入累计值"
        for j in range(df.shape[1]-2):
            line = go.Scatter(x=df['日期'],y=df.iloc[:,j+1],name=names[j+1])
            lst.append(line)
            
        line = go.Scatter(x=df['日期'],y=df.iloc[:,-1],xaxis='x',yaxis='y2',mode='lines',name=names[-1],marker=dict(color='grey'))
        lst.append(line)
        layout = go.Layout(yaxis2=dict(overlaying='y',side='right'),legend = dict(x=1.1,y=0.7,font=dict(family='sans-serif',size=18))) # 设置图例
        fig = go.Figure(lst, layout=layout)
        fig.update_layout(title=titles_net(data)[term])
        fig.show()


        
def Bar_net(data1,data2):
    dic1=net_buy(origin,datelist,paras,data1)
    participants1,terms,types,weekly,everyterm,everytype=paras[data1]
    
    dic2=net_buy(origin,datelist,paras,data2)
    participants2,terms,types,weekly,everyterm,everytype=paras[data2]
    
    # 对每个期限作图
    for term in terms:
        df1 = pd.DataFrame(dic1[term])
        df2 = pd.DataFrame(dic2[term])
        df = pd.concat([df1,df2.iloc[:,1:]],axis=1).iloc[-1,1:] # 横向合并两个表，取截面数据
        df = pd.DataFrame(df.T.sort_values(ascending=True)) # 排序
        names = list(df.index)
        for i in range(len(names)):
            names[i]=names[i][0:-6]
        trace = go.Bar(y=names,x=df.iloc[:,0],text=df.iloc[:,0],textposition='outside',orientation='h')
        fig = go.Figure(trace)
        fig.update_layout(title=titles_net2(data1)[term])
        fig.show()


def stack_net(data):
    dic=net_buy(origin,datelist,paras,data)
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    
    df = append_rates(dic['合计'],weekly,datelist)
    lst = []
    names = list(df.columns)
    for i in range(len(names)-1):
        names[i]=names[i][len(legend_dic[data]):-8] # 截取图例
    for j in range(df.shape[1]-2):
        trace = go.Bar(x=df['日期'],y=df.iloc[:,j+1],name=names[j+1])
        lst.append(trace)
    
    trace = go.Scatter(x=df['日期'],y=df.iloc[:,-1],xaxis='x',yaxis='y2',mode='lines',name=names[-1],marker=dict(color='grey'))
    lst.append(trace)
    layout = go.Layout(yaxis2=dict(overlaying='y',side='right'),barmode = 'stack',legend = dict(x=1.1,y=1,font=dict(family='sans-serif',size=16),traceorder='normal')) # 设置图例
    fig = go.Figure(lst, layout=layout)
    fig.update_layout(title=titles_spec(data))
    fig.show()
      
        
def stack_term(data):
    dic=net_buy(origin,datelist,paras,data)
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    
    # dic为dataframe,直接作图
    df = append_rates(dic,weekly,datelist)
    lst = []
    names = list(df.columns)
    for i in range(len(names)-1):
        names[i]=names[i][0:-8-len(legend_dic[data])] # 截取图例
    for j in range(df.shape[1]-2):
        trace = go.Bar(x=df['日期'],y=df.iloc[:,j+1],name=names[j+1])
        lst.append(trace)
        
    trace = go.Scatter(x=df['日期'],y=df.iloc[:,-1],xaxis='x',yaxis='y2',mode='lines',name=names[-1],marker=dict(color='grey'))
    lst.append(trace)
    layout = go.Layout(yaxis2=dict(overlaying='y',side='right'),barmode = 'stack',legend = dict(x=1.1,y=1,font=dict(family='sans-serif',size=16),traceorder='normal')) # 设置图例
    fig = go.Figure(lst, layout=layout)
    fig.update_layout(title=titles_term(data))
    fig.show()   



def stack_cross(data):
    dic=cs_net_buy(origin,paras,data)
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    
    # 对每个期限作图（dic为字典）
    for term in terms:
        df = pd.DataFrame(dic[term])
        df = df.sort_values(by='合计',ascending=True)
        lst = []
        names = list(df.columns)
        
        for i in range(df.shape[0]):
            df.iloc[i,-1]=float('%.2f' %df.iloc[i,-1])
        
        for j in range(df.shape[1]-3):
            trace = go.Bar(x=df.iloc[:,j+1],y=df['机构'],name=names[j+1],orientation='h')
            lst.append(trace)
            
        trace = go.Bar(x=df.iloc[:,-2],y=df['机构'],name=names[-2],orientation='h',text=df.iloc[:,-1],textposition='outside')
        lst.append(trace)
        layout = go.Layout(barmode = 'stack',legend = dict(x=1.1,y=0.9,font=dict(family='sans-serif',size=18))) # 设置图例
        fig = go.Figure(lst, layout=layout)
        fig.update_layout(title=titles_cross(data)[term])
        fig.show()
        
    
def titles_net(data):
    titles = {}
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    for term in terms:
        titles[term]=titles_dic[data]+'近一个月'+term+'净买入累计值'
    return titles

def titles_net2(data):
    titles = {}
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    for term in terms:
        titles[term]='各机构：近一个月'+term+'净买入累计值'
    return titles

def titles_spec(data):
    titles = titles_dic[data]+'各券种净增持规模'
    return titles


def titles_term(data):
    titles = titles_dic[data]+'各期限净增持规模'
    return titles

def titles_cross(data):
    titles = {}
    participants,terms,types,weekly,everyterm,everytype=paras[data]
    for term in terms:
        titles[term]='各机构'+term+'各券种净买入量'
    return titles


# In[7]:


title_date=dt.date.today().strftime('%Y-%m-%d') 
di.HTML('<div style="text-align:center; font-size:16px"><h1>机构现券成交跟踪 {}</h1></div>'.format(title_date))


# ## 近一个月净买入情况

# ### 交易户近一个月国债、政金债各期限累计买入规模

# In[8]:


line_net('data1')


# ### 配置户近一个月国债、政金债各期限累计买入规模

# In[9]:


line_net('data2')


# ### 各机构近1个月1Y+国债、政金债净买入累计值

# In[10]:


line_net('data3交易')
line_net('data3配置')

Bar_net('data3配置','data3交易')


# ### 各机构近1个月1Y-国债、政金债、同业存单净买入累计值

# In[11]:


line_net('data4交易')
line_net('data4配置')

Bar_net('data4交易','data4配置')


# In[12]:


#图6-13
sql=f'SELECT * FROM {db_name}.{table_name} where 交易类型 = \'net\';'
origin=mysql.read_table('guanc',sql)

#获取日期序列
datelist=sorted(list(set(origin['日期'].tolist())))


# ## 周度历史序列：分券种、期限净增持规模

# ### 各机构分券种净增持规模

# In[13]:


stack_net('data6')


# ### 基金全券种各期限净增持规模

# In[14]:


stack_term('data7')


# ### 基金利率债各期限净增持规模

# In[15]:


stack_term('data8')


# ### 基金各券种全部期限净增持规模

# In[16]:


stack_net('data9')


# ### 境外机构和外资行各期限净增持规模

# In[17]:


stack_term('data10')


# ### 境外机构和外资行分券种净增持规模

# In[18]:


stack_net('data11')


# ### 理财产品各期限净增持规模

# In[19]:


stack_term('data12')


# ### 理财产品各券种全部期限净增持规模

# In[20]:


stack_net('data13')


# ### 券商全券种各期限净增持规模

# In[21]:


stack_term('data14')


# ### 券商利率债各期限净增持规模

# In[22]:


stack_term('data15')


# ### 券商各券种全部期限净增持规模

# In[23]:


stack_net('data16')


# In[24]:


#图十七和十八横截面数据用新函数

sql=f'SELECT * FROM {db_name}.{table_name} as a,(select max(日期) as 日期 from guanc.net_incr_bond as b order by 日期 desc) as b where 交易类型 = \'net\' and a.日期=b.日期 ;'

origin=mysql.read_table('guanc',sql)
#dic=cs_net_buy(origin,paras,'data14')
#print(dic['1-3Y'])


# ## 利率债及存单最新日度净买入量

# ### 各机构分期限利率债日度净买入量（1Y+）

# In[25]:


stack_cross('data17')


# ### 各机构分期限利率债+同业存单日度净买入量（1Y-）

# In[26]:


stack_cross('data18')


# In[27]:

from IPython import get_ipython
get_ipython().system('jupyter nbconvert BondDaily.ipynb --template toc2')


# In[ ]:




