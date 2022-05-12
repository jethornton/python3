#!/usr/bin/env python3

import imaplib
address  = "cl@gnipsel.com"
password = "5J6PSLw8Zgx7B2dRcEVU"
imap  = imaplib.IMAP4_SSL('imap.dreamhost.com')
response, message = imap.login(address, password)
if response == 'OK':
	print('Logged In')

status, messages = imap.select("INBOX")
messages = int(messages[0])

