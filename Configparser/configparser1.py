#!/usr/bin/env python3

import sys, os
from configparser import ConfigParser

from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
	QVBoxLayout, QLabel, QPushButton, QAction)
from PyQt5.QtGui import QIcon

CFGPATH = os.path.join(os.path.expanduser('~'), ".config/config-example")

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('ConfigParser Example')

		widget = QWidget()

		# set the widget as the main window widget
		self.setCentralWidget(widget)

		# add a toolbar button to exit the application
		exitAction = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close)

		# create a vertical box layout
		vbox = QVBoxLayout()
		# set the layout to the widget
		widget.setLayout(vbox)

		vbox.addWidget(QLabel('Config Directory'))
		vbox.addWidget(QLabel(f'{CFGPATH}'))

		checkDirPB = QPushButton('Check Directory')
		checkDirPB.clicked.connect(self.checkDir)
		vbox.addWidget(checkDirPB)

		self.checkDirLB = QLabel()
		vbox.addWidget(self.checkDirLB)

		self.createDirPB = QPushButton('Create the Directory')
		self.createDirPB.setEnabled(False)
		self.createDirPB.clicked.connect(self.createDir)
		vbox.addWidget(self.createDirPB)

		self.createDirLB = QLabel()
		vbox.addWidget(self.createDirLB)

		checkFilePB = QPushButton('Check INI File')
		checkFilePB.clicked.connect(self.checkFile)
		vbox.addWidget(checkFilePB)

		self.checkFileLB = QLabel()
		vbox.addWidget(self.checkFileLB)

		self.createFilePB = QPushButton('Create the INI File')
		self.createFilePB.setEnabled(False)
		self.createFilePB.clicked.connect(self.createFile)
		vbox.addWidget(self.createDirPB)


		closeButton = QPushButton("Close")
		closeButton.clicked.connect(self.close)
		vbox.addWidget(closeButton)


		self.show()

	def checkDir(self):
		if os.path.isdir(CFGPATH):
			self.checkDirLB.setText('Directory Exists')
		else:
			self.checkDirLB.setText('Directory Does Not Exist')
			self.createDirPB.setEnabled(True)

	def createDir(self):
		os.makedirs(CFGPATH)
		self.createDirLB.setText('Directory Created')

	def checkFile(self):
		if os.path.isfile(os.path.join(CFGPATH, 'example.ini')):
			self.checkFileLB.setText('INI File Exists')
		else:
			self.checkFileLB.setText('INI File Does Not Exist')
			self.createFilePB.setEnabled(True)

	def createFile(self):
		pass

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())
