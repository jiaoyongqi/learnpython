# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

#to_list = ['123@123.com', '773163068@qq.com']
to_list =  ['773163068@qq.com']
server_host = 'smtp.163.com'

username = 'we1583004we@163.com'
password = '@#we1238@#we'


def send(to_list, sub, content):
  '''
  :param to_list: 收件人邮箱
  :param sub: 邮件标题
  :param content: 内容
  '''
  me = "manager" + "<" + username + ">"
  # _subtype 可以设为html,默认是plain
  msg = MIMEText(content, _subtype='html')
  msg['Subject'] = sub
  msg['From'] = me
  msg['To'] = ';'.join(to_list)
  try:
    server = smtplib.SMTP()
    server.connect(server_host)
    server.login(username, password)
    server.sendmail(me, to_list, msg.as_string())
    server.close()
    print "发送成功"
  except Exception as e:
    print str(e)
    print "发送失败"

if __name__ == '__main__':
  send(to_list, "这个是一个邮件", "<h1>Hello, It's  test email.</h1>")
