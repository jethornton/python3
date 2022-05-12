#!/usr/bin/env python3
import imaplib

def receive_imap_email(imap_server, user, password):
	imap = imaplib.IMAP4_SSL(imap_server)
	imap.login(user, password)
	response, data = imap.list()
	print(response)
	print(data[0])
	print(data[1:3])
	response, data = imap.select('INBOX')
	print(response)
	print(data)
	imap.select(settings.EMAIL_GATEWAY_IMAP_FOLDER)
	status, num_ids_data = imap.search(None, 'ALL')
	for id in ids:
		res, featch_data = imap.fetch(str.encode(str(id)), '(RFC822)')
		print(res)
		if featch_data[0] is not None:
			for part in email.message_from_string(str(featch_data[0][1])).walk():
				print(part.get_payload(decode=True))

receive_imap_email('imap.dreamhost.com', 'cl@gnipsel.com', '5J6PSLw8Zgx7B2dRcEVU')
