#!/usr/bin/env python3

#modules
import imaplib
import email

#credentials
user ="cl@gnipsel.com"

#generated app password
password= "5J6PSLw8Zgx7B2dRcEVU"

# https://www.systoolsgroup.com/imap/
host= 'imap.dreamhost.com'

#set connection
mail = imaplib.IMAP4_SSL(host)

#login
mail.login(user, password)

#select inbox
mail.select("INBOX")

#select specific mails
_, selected_mails = mail.search(None, '(FROM "noreply@kaggle.com")')

#total number of mails from specific user
print("Total Messages from noreply@kaggle.com:" , len(selected_mails[0].split()))

for num in selected_mails[0].split():
	_, data = mail.fetch(num , '(RFC822)')
	_, bytes_data = data[0]

	#convert the byte data to message
	email_message = email.message_from_bytes(bytes_data)
	print("\n===========================================")

	#access data
	print("Subject: ",email_message["subject"])
	print("To:", email_message["to"])
	print("From: ",email_message["from"])
	print("Date: ",email_message["date"])
	for part in email_message.walk():
		if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
			message = part.get_payload(decode=True)
			print("Message: \n", message.decode())
			print("==========================================\n")
			break
