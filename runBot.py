# Terrible
import os
import httplib

running = True

while True:
	try:
		os.system('python bot.py')
	except e:
		running = False
		stream.disconnect()
		print(e)
	except httplib.IncompleteRead:
		print("Incomplete Read occurred --> continuing")
		running = True
		continue
	except KeyboardInterrupt:
		print("\n\nUser disconnected stream")
		stream.disconnect()
		running = False
		break

