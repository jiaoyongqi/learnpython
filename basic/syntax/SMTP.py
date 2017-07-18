# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'we1583004we@163.com'
# receivers = ['773163068@qq.com']
#
# server_host = 'smtp.163.com'
#
# username = 'we1583004we@163.com'
# password = '@#we1238@#we'
#
# # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
# try:
#      smtpObj = smtplib.SMTP()
#      smtpObj.connect(server_host)
#      smtpObj.login(username,password)
#      smtpObj.sendmail(sender, receivers, message.as_string())
#      smtpObj.close()
#      print "邮件发送成功"
# except smtplib.SMTPException:
#      print "Error: 无法发送邮件"



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
    print "发生失败"

if __name__ == '__main__':
  send(to_list, "这个是一个邮件", "<h1>Hello, It's test email.</h1>")
