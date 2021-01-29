#!/usr/bin/python3

"""
sudo apt install python3-schedule
"""

import signal, schedule
from PyQt5.QtCore import QTimer


class main():
	def __init__(self, parent=None):
		print('starting')
		# catch ctrl c and run cleanExit
		signal.signal(signal.SIGINT, self.cleanExit)
		schedule.every().second.do(self.run)

	def run(self):
		schedule.run_pending()
		print('press ctrl c to exit')

	def cleanExit(self):
		print('\nClean Exit')
		sys.exit()

if __name__ == '__main__':
	main()
