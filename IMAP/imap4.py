#!/usr/bin/env python3

import datetime
import email
import imaplib
import mailbox
import re

EMAIL_ACCOUNT = "cl@gnipsel.com"
PASSWORD = "5J6PSLw8Zgx7B2dRcEVU"
mail = imaplib.IMAP4_SSL('imap.dreamhost.com')
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.select('INBOX')
result, data = mail.search(None, '(FROM "robot@craigslist.org")','ALL')
#result, data = mail.search(None, '(SUBJECT "Message")','ALL')
i = len(data[0].split())

if i == 1:
	latest_email_uid = data[0].split()[0]
	result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	raw_email = email_data[0][1]
	raw_email_string = raw_email.decode('utf-8')
	email_message = email.message_from_string(raw_email_string)
	body = email_message.get_payload(decode=True)
	for part in email_message.walk():
		if part.get_content_type() == "text/plain":
		 emailBody = part.get_payload(decode=True)
		 print(emailBody)            
		else:
		 continue
else:
	print('Email NOT ' + EMAIL_ACCOUNT  )
