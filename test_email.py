import smtplib
import getpass

gmail_user = 'mgdevtest@gmail.com'
#gmail_password = ''



try:
    gmail_password = input("Password: ")
    
except:
    print("error")

#TODO -- better method of password input and masking

sent_from = gmail_user
to = ['mgordon25@gmail.com']
subject = 'Daily report'
body = 'Here is the daily report'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" %(sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to , email_text)
    server.close()
    

    print('Email sent')

except:
    print('Somthing went wrong...')
