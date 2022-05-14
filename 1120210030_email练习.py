import email
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...','plain','utf-8')
#输入email地址和口令
from_addr=input('from:')
password=input('password:')
#输入smtp服务器地址
smtp_server=input('smtp server:')
#输入收件人地址
to_addr=input('to:')

server=smtplib.SMTP(smtp_server,25)#SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
