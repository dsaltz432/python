'''
Used for checking a backpacking booking website
Periodically checks the website to see if there are any availablities
Writes the results to bookings.txt
If there are any changes that I predetermined to be worth noting, send me an email with the changes

'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import datetime
import urllib2
from bs4 import BeautifulSoup


def sendEmail() :
	me = "dsaltz190@gmail.com"
	you = "dsaltz190@gmail.com"

	# insert password before using
	password = "****"

	msg = MIMEMultipart()
	msg.attach(MIMEText(file("bookings.txt").read()))
	msg['Subject'] = "RouteburnScript"
	msg['From'] = me
	msg['To'] = you

	# attach the text file
	attachment = MIMEText(f.read())
	attachment.add_header('Content-Disposition', 'attachment', filename="bookings.txt")           
	# msg.attach(attachment)

	# send the email
	mail = smtplib.SMTP('smtp.gmail.com','587')
	mail.ehlo()
	mail.starttls()
	mail.login(me,password)
	mail.sendmail(me,you,msg.as_string())
	mail.quit()

def runScript():

	# load site into soup object
	soup = BeautifulSoup(urllib2.urlopen('https://booking.doc.govt.nz/AvailabilityDisplay.aspx?sg=RBN&sd=20/04/16&mp=1').read(),"html.parser")

	# find the exact cells of interest
	bookingTable = soup.find(id="availabilityTableInnerDiv")

	# gets the data for Lake Mackenzie hut for 4/20
	mackenzieRow = bookingTable.find(id = "ctl00_ctl00_bCPH_mCPH_availabilityView_ctrl2_detailRow")
	mackenzieHutOn20 = mackenzieRow.find(id="ctl00_ctl00_bCPH_mCPH_availabilityView_ctrl2_Label3").contents

	# gets the data for Routeburn Falls Hut for 4/21
	routeburnFallsRow = bookingTable.find(id = "ctl00_ctl00_bCPH_mCPH_availabilityView_ctrl1_detailRow")
	routeburnFallsOn21 = routeburnFallsRow.find(id="ctl00_ctl00_bCPH_mCPH_availabilityView_ctrl1_Label3").contents

	# get current day to put in text file
	now = datetime.datetime.now()
	date = str(now.month)+"/"+str(now.day)+ " "+ str(now.hour)+":"+str(now.minute)

	# create/read file to store results
	f = open("bookings.txt","r+")

	for line in f:
		lastLine = line.split(",")
		mackenzieCell = int(lastLine[2])
		routeburnFallsCell = int(lastLine[4])

	# logging data, and emailing if there's a change
	if (int(mackenzieHutOn20[0]) != mackenzieCell or int(routeburnFallsOn21[0]) != routeburnFallsCell):
		f.write("\n"+date+", mackenzie hut for 4/20, " +mackenzieHutOn20[0]+
			", routeburn falls hut for 4/21, "+routeburnFallsOn21[0])
		# print "change!"
		sendEmail()
	else:
		# print "no change"
		f.write("\n"+date+", mackenzie hut for 4/20, " +mackenzieHutOn20[0]+
		", routeburn falls hut for 4/21, "+routeburnFallsOn21[0])

	f.close()


while(True):
	runScript()
	time.sleep(1000)

