#! /usr/bin/env python3

import imaplib
import email
from email.header import decode_header
import HTMLParser


# to unescape xml entities
_parser = HTMLParser.HTMLParser()

def decodeHeader(value):
	if value.startswith('"=?'):
		value = value.replace('"', '')

	value, encoding = decode_header(value)[0]
	if encoding:
		value = value.decode(encoding)

	return _parser.unescape(value)

def listLastInbox(top = 4):
	mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
	mailbox.login('mygmail@gmail.com', 'somecrazypassword')

	selected = mailbox.select('INBOX')
	assert selected[0] == 'OK'
	messageCount = int(selected[1][0])

	for i in range(messageCount, messageCount - top, -1):
		reponse = mailbox.fetch(str(i), '(RFC822)')[1]
		for part in reponse:
			if isinstance(part, tuple):
				message = email.message_from_string(part[1])
				yield {h: decodeHeader(message[h]) for h in ('subject', 'from', 'date')}

	mailbox.logout()


if __name__ == '__main__':
	for message in listLastInbox():
		print( '-' * 40)
		for h, v in message.items():
			print( u'{0:8s}: {1}'.format(h.upper(), v))
