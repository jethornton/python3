Keyboard Routines
=================

Capture keystrokes
::

	#!/usr/bin/env python3

	"""
	Capture a single character of input without waiting for the user to
	press enter

	Exit on ctrl c, ctrl d, ctrl x or ctrl z

	(OS is Linux
	"""

	import tty, sys, termios

	class ReadChar():
		def __enter__(self):
			self.fd = sys.stdin.fileno()
			self.old_settings = termios.tcgetattr(self.fd)
			tty.setraw(sys.stdin.fileno())
			return sys.stdin.read(1)
		def __exit__(self, type, value, traceback):
			termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

	def test():
		while True:
			with ReadChar() as rc:
				char = rc
			if ord(char) <= 32:
				print(f"You entered non printing character ordinal: {ord(char)}.")
				# ctrl c, ctrl d, ctrl x or ctrl z will exit
				if ord(char) in [3, 4, 24, 26]:
						sys.exit()

			else:
					print(f"You entered character '{char}'.")

	if __name__ == "__main__":
		test()

