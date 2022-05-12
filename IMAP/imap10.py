#!/usr/bin/env python3

import imaplib

address = 'cl@gnipsel.com'
password = '5J6PSLw8Zgx7B2dRcEVU'
server= imaplib.IMAP4_SSL('imap.dreamhost.com')
server.login(address, password)
server.list()
server.select()
typ, data = server.search(None, 'ALL')

for num in data[0].split():
	typ, data = server.fetch(num, '(RFC822)')

server.close()
server.logout()


m1 = data[0].split()[0]
typ, data = server.fetch(m1, '(RFC822)')
