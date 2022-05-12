#! /usr/bin/env python3

import imaplib
#import base64
import os
import email

email_user = "cl@gnipsel.com"
email_pass = "5J6PSLw8Zgx7B2dRcEVU"
mail = imaplib.IMAP4_SSL("imap.dreamhost.com", 993)
mail.login(email_user, email_pass)
mail.select()
type, data = mail.search(None, 'ALL')
mail_ids = data[0].decode('utf-8')
id_list = mail_ids.split()
mail.select('INBOX', readonly=True)
for i in id_list:
	typ, msg_data = mail.fetch(str(i), '(RFC822)')
	for response_part in msg_data:
		if isinstance(response_part, tuple):
			msg = email.message_from_bytes(response_part[1])
			print(msg['from']+"\t"+msg['subject'])
