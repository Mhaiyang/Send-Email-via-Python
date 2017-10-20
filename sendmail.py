import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

me_path = "me.txt"
# me_path = os.path.join('send_message', "me.txt")
with open(me_path) as f:
    setting = f.readlines()
    EMAIL_NAME = setting[0]
    SECRET_KEY = setting[1]

mail_host="smtp.qq.com"  #设置服务器
mail_user=EMAIL_NAME    #用户名
mail_pass=SECRET_KEY   #口令 

def send(name, emailaddr, content, subject):
    sender = mail_user
    receivers = [emailaddr]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mail_msg = content
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = mail_user
    message['To'] =  emailaddr
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL() 
        smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return name+"发送成功"
    except smtplib.SMTPException:
        return name+"邮件发送失败！！！"
