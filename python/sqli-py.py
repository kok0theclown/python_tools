import subprocess
import numpy as np
import sys

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	RESETALL = "\033[0m"

if len(sys.argv) != 3:
	print(bcolors.OKGREEN+"Usage:")
	print(bcolors.RESETALL+bcolors.OKGREEN+"        python3 sqli-py.py http://<IP>/whatever.php?search= 'COOKIE=xd'" )
	print("")
	exit()

url = sys.argv[1]

print(bcolors.OKGREEN+"URL: "+url)
if len(sys.argv) == 3:
	print(bcolors.OKGREEN+"COOKIE: "+sys.argv[2])


while(True):
	print(bcolors.OKGREEN + bcolors.BOLD + " > "+bcolors.RESETALL, end="")
	command = input()
	if command == "exit":
        	exit()

	curl = ""
	#if command has cookies
	if len(sys.argv) == 3:
    		curl = np.hstack(("curl","-b",sys.argv[2],"-s","-X","GET", (url+(command.replace(" ", "+"))),"|","html2text"))
	#else command has cookies
	else:
		curl = np.hstack(("curl","-s","-X","GET", (url+(command.replace(" ", "+"))),"|","html2text"))
	# curl = np.hstack( ("curl","-s","-X","GET", (url+(command.replace(" ", "%20"))) ) )
	print(curl)
	try:
		subprocess.call(curl)
	except:
		print(bcolors.FAIL + "Error")

