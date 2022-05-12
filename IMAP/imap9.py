#!/usr/bin/env python3
import imaplib

def get_imap(server, sender, user):
	result = FAIL
	try:
		box = imaplib.IMAP4_SSL(server)
		box.login(*user)
		box.select()
		typ, data = box.search(None, 'FROM', '"{0}"'.format(sender[0]))
		for num in data[0].split():
			typ, data = box.fetch(num, '(RFC822)')
			if content.format(sender[0]) in data[0][1]:
				result = OK
			box.store(num, '+FLAGS', '\\Deleted')

		box.expunge()
		box.close()
		box.logout()
		return result
	except Exception as e:
		print("IMAP error: {0}".format(e))
		#return FAIL

get_imap('imap.dreamhost.com', 'cl@gnipsel.com', '5J6PSLw8Zgx7B2dRcEVU')
