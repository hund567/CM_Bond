# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime


def sendmail(file_path,sender,receivers):
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "hund567"  # 用户名
    mail_pass = "1990312peking"  # 口令

    # 创建一个带附件的实例
    message = MIMEMultipart()
    today = datetime.datetime.today().date()
    # message['From'] = Header(str(today)+"债券市场综合报表", 'utf-8')
    subject = str(today)+"债券市场综合报表"
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    # message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件

    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    filename = str(today)+"BondDaily.html"
    att1["Content-Disposition"] = 'attachment; filename='+filename
    message.attach(att1)

    # # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)
if __name__ == '__main__':
    sender = 'hund567@163.com'
    receivers = ['hund567@163.com',"227362424@qq.com","wingyylr@163.com","linyingyingalm@cmbchina.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 并且注意receivers是个list里面可以放多个目标邮箱地址
    sendmail("C:\\Users\\hund567\\Desktop\\CM_BOND\\BondDaily-v2.html",sender,receivers)
