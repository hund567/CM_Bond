# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime


def sendmail(file_path, sender, receivers):
    #
    mail_host = "smtp.sina.com"  # 设置服务器
    mail_user = "potatooo43@sina.com"  # 用户名
    mail_pass = "15dd9bdca5326b72"  # 口令

    # 创建一个带附件的实例
    message = MIMEMultipart()
    today = datetime.datetime.today().date()
    message['From'] = mail_user
    subject = str(today) + "债券市场综合报表"
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    # message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件

    att1 = MIMEText(open(file_path + "BondDaily-v4.html", 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    filename = str(today) + "_BondDaily_js.html"
    print(filename)
    att1["Content-Disposition"] = 'attachment; filename=' + filename
    message.attach(att1)

    # # 构造附件2，传送当前目录下的 runoob.txt 文件
    att2 = MIMEText(open(file_path + "BondDaily-v4-without-js.html", 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    filename = str(today) + "_BondDaily_without_js.html"
    print(filename)
    att2["Content-Disposition"] = 'attachment; filename=' + filename
    message.attach(att2)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)


if __name__ == '__main__':
    sender = 'potatooo43@sina.com'
    receivers = ['hund567@163.com', "227362424@qq.com", "wingyylr@163.com",
                 "linyingyingalm@cmbchina.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 并且注意receivers是个list里面可以放多个目标邮箱地址
    file_path = "C:\\Users\\Administrator\\Desktop\\html\\"
    sendmail(file_path, sender, receivers)
