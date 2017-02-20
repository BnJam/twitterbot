import os

running = True

while True:
	try:
		os.system('python bot.py')
	except e:
			print(e)
			running = False
	running = True
