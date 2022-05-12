#!/usr/bin/env python3
import imaplib

def check(user, passwd):
	try:
		mail = imaplib.IMAP4_SSL("imap.dreamhost.com")
		mail.login(user, passwd)
	except imaplib.IMAP4.error as ex:
		log(ex)
		sys.exit(1)
	mail.select()
	status, response = mail.search(None, 'ALL')
	mailids = [int(a) for a in response[0].split()]
	my_mailid = model.DB.get().max_mailid()
	new_mailids = [a+1 for a in range(my_mailid, max(mailids))]

	for mailid in new_mailids:
		log("I'm at: " + str(mailid))
		f = i.fetch(mailid, '(RFC822)')
		mail = f[1][0][1]
		info = f[1][0][0]
		process(mail)
		model.DB.get().add_mailid(mailid)

	i.close()
	i.logout()

check('cl@gnipsel.com', '5J6PSLw8Zgx7B2dRcEVU')
