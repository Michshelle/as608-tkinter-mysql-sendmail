import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

def send_email(subject_content):
    # 邮箱配置
    smtp_server = os.environ.get('SMTPSERVER')
    smtp_port = 587                      # 常用端口：465/587
    sender = os.environ.get('ADMINMAIL')  # 发件人邮箱
    password = os.environ.get('PWQQ')     # 发件人邮箱密码或授权码
    receiver = os.environ.get('BOSSMAIL') # 收件人邮箱

    # 构造邮件
    subject_content = "[jiajialing]" + subject_content
    msg = MIMEText(subject_content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject_content, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
    except Exception as e:
        pass