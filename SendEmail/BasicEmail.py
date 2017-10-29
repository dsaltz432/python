
'''
This program sends an email with a Subject and Body of text

'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail() :
	me = "dsaltz190@gmail.com"
	you = "dsaltz190@gmail.com"

	# insert password before using
	#password = ""

	msg = MIMEMultipart()
	msg['Subject'] = "This is the subject"
	msg['From'] = me
	msg['To'] = you

	# add body
	msg.attach(MIMEText("Hello, " + you, 'plain'))

	# send the email
	mail = smtplib.SMTP('smtp.gmail.com','587')
	mail.ehlo()
	mail.starttls()
	mail.login(me,password)
	mail.sendmail(me,you,msg.as_string())
	mail.quit()

sendEmail()



