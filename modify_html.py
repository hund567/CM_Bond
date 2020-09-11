#!/usr/bin/python3.8.5
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def modify_html(html_file):
    content = open(html_file, 'r', encoding="utf-8")
    html_cont = content.read()
    find_content = BeautifulSoup(html_cont, 'lxml')
    src_list = ["./require.min.js", "./jquery.min.js"]
    label_list = find_content.findAll('script')
    i = 0
    for label in label_list:
        label["src"] = src_list[i]  # src_list[i]类型也是<class 'bs4.element.Tag'>
        i += 1
        if i == 2:
            break

    #删除掉最后一个pre对象
    label_list_pre = find_content.findAll('pre')

    remove_list = ["[NbConvertApp] WARNING","This application is used to convert"]

    for each_remove_line in remove_list:
        i = 0
        for each in label_list_pre:
            if each_remove_line  in str(each):
                tag_num = i
                break
            i = i + 1

        new_tag = find_content.new_tag("pre")
        new_tag.string = ""
        # `replace_with` 方法来替换掉
        find_content.find_all('pre')[tag_num].replace_with(new_tag)

    # 最后将其写入
    with open(html_file, 'w') as fp:
        fp.write(find_content.prettify())


if __name__ =="__main__":
    modify_html("/Users/hund567/Downloads/2020-09-11_BondDaily.html")
