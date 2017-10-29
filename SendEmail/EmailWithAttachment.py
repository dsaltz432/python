
'''
This program sends an email with a Subject, Body, and text file attachment

'''

import smtplib
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import Encoders

def sendEmail() :
	me = "dsaltz190@gmail.com"
	you = "saglick@brandeis.edu"

	# insert password before using
	#password = ""

	msg = MIMEMultipart("mixed")
	msg['Subject'] = "testing"
	msg['From'] = me
	msg['To'] = you

	# add body
	msg.attach(MIMEText("Hello, " + you + ". Sent by python", 'plain'))


	# attach the text file
	fileName = "attachment.txt"
	attachment = MIMEBase('application', "octet-stream")
	attachment.set_payload(open(fileName, "rb").read())
	Encoders.encode_base64(attachment)
	attachment.add_header('Content-Disposition', 'attachment; filename='+fileName)
	msg.attach(attachment)

	# send the email
	mail = smtplib.SMTP('smtp.gmail.com','587')
	mail.ehlo()
	mail.starttls()
	mail.login(me,password)
	mail.sendmail(me,you,msg.as_string())
	mail.quit()

sendEmail()



