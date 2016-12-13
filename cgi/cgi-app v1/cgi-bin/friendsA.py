#!/usr/bin/env python3
import cgi

# \n用于分割http的 head 和 body
res_html = '''Content-Type: text/html\n
<!DOCTYPE html>
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
</html>'''


form = cgi.FieldStorage()
name = form['person'].value
friend_number = form['howmany'].value
print(res_html % (name, name, friend_number))
