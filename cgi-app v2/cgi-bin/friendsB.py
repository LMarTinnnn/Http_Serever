#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

http_header = 'Content-Type: text/html\n'

# 注意第十八行的不可见input 用于检测是否有表格被提交
form_html = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Friends CGI DEMO(static)</title>
  </head>
  <body>
    <h1>Friends list for: <i>New User</i></h1>
    <form action="/cgi-bin/friendsB.py">
      <div class="username">
        <b>Enter your name: </b>
        <input type="hidden" name="action" value="edit">
        <input type="text" name="person" size="15" placeholder="user name">
      </div>
      <div class="number">
        %s
      </div>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
'''


def show_form():
    input_format = '<input type="radio" name="number" value="%s" %s> %s'
    inputs = []
    checked = ''
    for i in [0, 10, 25, 50, 100]:
        if i == 0:
            checked = 'CHECKED'
        inputs.append(input_format % (str(i), checked, str(i)))
    print(http_header)
    print(form_html % ''.join(inputs))


res_html = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Friends CGI Demo (dynamic screen)</title>
  </head>
  <body>
    <h1>Friend list for : <i>%s</i></h1>
    <p>Your name is: <b>%s</b></p>
    <p>You have <b>%s</b> friends</p>
  </body>
</html>
'''


def do_result(name, number):
    print(http_header)
    print(res_html % (name, name, number))


def run():
    # 动态选择生成的html
    form = cgi.FieldStorage()

    if 'action' in form:
        # 呼应第十八行埋的伏笔 检测是否有表格提交
        name = form['person'].value
        number = form['number'].value
        do_result(name, number)
    else:
        show_form()

if __name__ == '__main__':
    run()
