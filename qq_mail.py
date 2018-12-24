import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
my_sender = 'xxxxxxx@qq.com'  # 发件人邮箱账号
my_pass = 'password_your'       # 发件人邮箱密码(当时申请smtp给的口令)
my_user = 'xxxxddddd@qq.com'   # 收件人邮箱账号，我这边发送给自己
my_contents='we the '
msg = MIMEMultipart() 
print(os.path.getsize('test.py')/1024,'kb')
def mail():
  ret = True
  try:
    msg0 = MIMEText(open('test.py', 'rb').read(), 'base64', 'utf-8')
    msg0["Content-Type"] = 'application/octet-stream'
    msg0["Content-Disposition"] = 'attachment; filename="test.py"'
    msg.attach(msg0)
    msg1 = MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
    msg1["Content-Type"] = 'application/octet-stream'
    msg1["Content-Disposition"] = 'attachment; filename="mail.txt"'
    msg.attach(msg1)
    #  多个附件时不停添加即可
    msg2=MIMEText(my_contents,'plain','utf-8')
    msg['From']=formataddr([my_sender, my_sender]) 
     # 括号里的对应发件人邮箱昵称、发件人邮箱账号
     #  此处的msg一定要和msg.as_string相等
    msg['To']=formataddr([my_user, my_user])       
     # 括号里的对应收件人邮箱昵称、收件人邮箱账号
     #  此处的msg一定要和msg.as_string相等
    msg['Subject']= '邮件主题'     
     # 邮件的主题
     #  此处的msg一定要和msg.as_string相等
    msg.attach(msg2)
    server=smtplib.SMTP_SSL("smtp.qq.com", 465) 
     # 发件人邮箱中的SMTP服务器，端口是465
    server.login(my_sender, my_pass) 
     # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender, [my_user,], msg.as_string()) 
     # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit() # 关闭连接
  except Exception: # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    ret = False
  return ret
 
ret = mail()
if ret:
  print("邮件发送成功")
else:
  print("邮件发送失败")
