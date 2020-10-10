Event Loop
==========

Event loop that executes every n seconds
::

	#!/usr/bin/python3

	import asyncio
	import signal

	def main():
		loop = asyncio.get_event_loop()
		asyncio.ensure_future(listen_to_ipc_channel_layer())

		for sig in (signal.SIGINT, signal.SIGTERM):
			loop.add_signal_handler(sig, ask_exit)
		loop.run_forever()
		print("Close")
		loop.close()

	@asyncio.coroutine
	def listen_to_ipc_channel_layer():
		while True:
			try:
				#print("Running")
				run()
				yield from asyncio.sleep(0.1)
			except asyncio.CancelledError as e:
				print("\nBreak it out")
				raise e # Raise a proper error

	# Stop the loop concurrently
	@asyncio.coroutine
	def exit():
		loop = asyncio.get_event_loop()
		print("Stop")
		loop.stop()

	def ask_exit():
		for task in asyncio.Task.all_tasks():
			task.cancel()
		asyncio.ensure_future(exit())

	# check the I/O for changes
	def run():
		#print('run')
		print(f'keypress {poll()}')

	if __name__ == "__main__":               
		main()                            
