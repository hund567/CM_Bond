#!/usr/bin/python3.8.5
# -*- coding: utf-8 -*-

import imaplib
from email.header import decode_header
import email
mailServer = "imap.sina.com"

mailUser= "potatooo43@sina.com"
mailPassWord = "15dd9bdca5326b72"

def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def parseEmail(msg, base_save_path):
    #循环信件中的每一个mime的数据块
    content = ''
    attachment_files = []
    for part in msg.walk():
        if not part.is_multipart(): # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
            contentType=part.get_content_type()
            filename=part.get_filename()
            if filename:
                # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
                h = email.header.Header(filename, charset='utf-8')
                dh = email.header.decode_header(h)
                filename = dh[0][0]
                if dh[0][1]:  # 如果包含编码的格式，则按照该格式解码
                    filename = str(filename, dh[0][1])
                    filename=decode_str(filename)
                data = part.get_payload(decode=True) #　解码出附件数据，然后存储到文件中
                att_file = open(base_save_path + filename, 'wb')
                attachment_files.append(filename)
                att_file.write(data)
                att_file.close()
            elif contentType == 'text/plain' or contentType == 'text/html':
                # 保存正文
                data = part.get_payload(decode=True)
                charset = guess_charset(part)
                if charset:
                    charset = charset.strip().split(';')[0]
                    data = data.decode(charset)
                content = data

    return content, attachment_files

def main():
    # login
    #while 1:
       #imapServer = imaplib.IMAP4(mailServer)
    imapServer = imaplib.IMAP4_SSL(mailServer, 993)
    imapServer.login(mailUser, mailPassWord)
    imapServer.select()
    base_save_path = '/Users/xxx/PycharmProjects/'
    # list items on server
    #resp, items = imapServer.search(None, "ALL")   #all Message.
   #Seen   unSeen
    mailResp, mailItems = imapServer.search(None, "unSeen")
  #  #resp, items = imapServer.search(None, "Seen")  #Message has been read.
    #resp, items = imapServer.search(None, "Answered")   #Message has been answered.
    #resp, items = imapServer.search(None, "Flagged")   #Message is "flagged" for urgent/special attention.
    #resp, items = imapServer.search(None, "Deleted")   ##python无法看到已删除邮件   
    #resp, items = imapServer.search(None, "Draft") ##python无法看到草稿箱内的邮件
    for i in mailItems[0].split():
        resp, mailData = imapServer.fetch(i, "(RFC822)")##读取邮件信息
        mailText = mailData[0][1]
        mail_message = email.message_from_string(mailText.decode(encoding='utf-8'))

        content, attachment_files  = parseEmail(mail_message, base_save_path)
        print(attachment_files)

    imapServer.close()
    imapServer.logout()
    # time.sleep(0)
    """
     mailFile = StringIO.StringIO(mailText)
     mailMessage = rfc822.Message(mailFile)
     newMail = dict(mailMessage.items())
     mailMessage.fp.read()
    #server.store(items[i], '+FLAGS', '\\Deleted')##删除指定的一份邮件
    """
if __name__ =="__main__":
    main()
