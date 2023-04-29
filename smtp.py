#!/usr/bin/bash

import smtplib

rec_mail = input("Please enter the recipient mail address: ")
mail_header = input("please enter your massage header: ")
message = input('please enter your mail massage: ')

smtp_serv = 'sandbox.smtp.mailtrap.io'
port = 587
username = input("please enter your username : ")
password = input("please enter your password: ")
my_mail = input("please enter your mail account : ")

with smtplib.smtp(smtp_serv, port) as server:
    server.starttls()
    server.login(username, password)
    email_message = f'mail_header: {mail_header}\n\n{message}'
    server.sendmail(my_mail, rec_mail, email_message)

print("Email sent successfully!")
