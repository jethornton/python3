#!/usr/bin/env python3

import imaplib
import email
from email.header import decode_header

username = "cl@gnipsel.com"
password = "5J6PSLw8Zgx7B2dRcEVU"
mail = []

try:
	imap = imaplib.IMAP4_SSL("imap.dreamhost.com")
except:
	print('Error Connecting to Host')
# authenticate
response, data = imap.login(username, password)
print(f'Login: {response}')

status, messages = imap.select("INBOX")
#print(f'Select: {status}')

# total number of emails converted to int
messages = int(messages[0])

# number of top emails to fetch
top = 1
for i in range(messages, messages - top, -1):
	# fetch the email message by ID
	response, msg = imap.fetch(str(i), "(RFC822)")
	#print(f'Fetch: {response}')

	for response in msg:
		if isinstance(response, tuple):
			# parse a bytes email into a message object
			msg = email.message_from_bytes(response[1])
			# decode the email subject
			subject, encoding = decode_header(msg["Subject"])[0]
			if isinstance(subject, bytes):
				# if it's a bytes, decode to str
				subject = subject.decode(encoding)
			#print(f'Subject: {subject}')
			mail.append({'ID': i, 'Subject': subject})

			# decode email sender
			From, encoding = decode_header(msg.get("From"))[0]
			if isinstance(From, bytes):
				From = From.decode(encoding)
			a = From.rfind('<')
			address = From[a+1:-1]
			n = From.rfind('"')
			name = From[1:n]
			print(f'Name: {name}')
			print(f'Address: {address}')

			# decode date
			Date, encoding = decode_header(msg.get("Date"))[0]
			if isinstance(Date, bytes):
				Date = Date.decode(encoding)
			print(f'Date: {Date}')

			# if the email message is multipart
			if msg.is_multipart():
				print('is_multipart')
				# iterate over email parts
				for part in msg.walk():
					# extract content type of email
					content_type = part.get_content_type()
					content_disposition = str(part.get("Content-Disposition"))
					try:
						# get the email body
						body = part.get_payload(decode=True).decode()
					except:
						pass
					if content_type == "text/plain" and "attachment" not in content_disposition:
						# print text/plain emails and skip attachments
						print(body)
					elif "attachment" in content_disposition:
						# download attachment
						filename = part.get_filename()
						if filename:
							folder_name = clean(subject)
							if not os.path.isdir(folder_name):
								# make a folder for this email (named after the subject)
								os.mkdir(folder_name)
							filepath = os.path.join(folder_name, filename)
							# download attachment and save it
							open(filepath, "wb").write(part.get_payload(decode=True))
			else:
				print('not multipart')
				# extract content type of email
				content_type = msg.get_content_type()
				# get the email body
				body = msg.get_payload(decode=True)
				if content_type == "text/plain":
					# print only text email parts
					print(body)
			if content_type == "text/html":
				print('text/html')
				# if it's HTML, create a new HTML file and open it in browser
				folder_name = clean(subject)
				if not os.path.isdir(folder_name):
					# make a folder for this email (named after the subject)
					os.mkdir(folder_name)
				filename = "index.html"
				filepath = os.path.join(folder_name, filename)
				# write the file
				open(filepath, "w").write(body)
				# open in the default browser
				webbrowser.open(filepath)
			print("="*100)

response, data = imap.close() # close the selected mailbox
# ('OK', [b'Close completed (0.001 + 0.000 + 0.021 secs).'])
response, data = imap.logout() # logout of the connection
# ('BYE', [b'Logging out'])
