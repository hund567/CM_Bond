#!/usr/bin/python3.8.5
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def modify_html(html_file):
    content = open(html_file, 'r', encoding="utf-8")
    html_cont = content.read()
    find_content = BeautifulSoup(html_cont.replace('&nbsp;', ' '), 'lxml')

    label_list_pre = find_content.findAll('pre')
    remove_list = ["[NbConvertApp] WARNING", "This application is used to convert"]

    for each_remove_line in remove_list:
        i = 0
        for each in label_list_pre:
            if each_remove_line in str(each):
                tag_num = i
                break
            i = i + 1

        new_tag = find_content.new_tag("pre")
        new_tag.string = ''
        find_content.find_all('pre')[tag_num].replace_with(new_tag)

    with open(html_file, 'w', encoding="utf-8") as fp:
        fp.write(find_content.prettify())

    src_list = ["./require.min.js", "./jquery.min.js"]
    label_list = find_content.findAll('script')
    i = 0
    for label in label_list:
        label["src"] = src_list[i]
        i += 1
        if i == 2:
            break
    with open(file_path + "BondDaily-v4-without-js.html", 'w', encoding="utf-8") as fp:
        fp.write(find_content.prettify())


if __name__ == "__main__":
    file_path = "C:\\Users\\Administrator\\Desktop\\html\\"
    file_name = "BondDaily-v4.html"
    modify_html(file_path + file_name)