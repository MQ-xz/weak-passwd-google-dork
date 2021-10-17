#!/usr/bin/python3
 #A simple port scanner created by Akshay Ravi

import socket
import os
import subprocess
from termcolor import colored
 
os.system("clear")

subprocess.call('figlet "Port Scan"' , shell=True)
print("-" * 45)
print("A Simple Port Scanner Created By Akshay Ravi")
print("-" * 45 )
  #socket for connection & AF_INET for ipv4  & SOCK_STREAM for specifying the connection
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

host=input("[*]Entet IP : " )
port=int(input("[*]Enter Port: "))
 
def portScanner(port):
	if s.connect_ex((host , port)):
	    print(colored("[*]The port is closed" , 'red'))
	else:
		print(colored("[*]The port is open" , 'yellow'))
	
portScanner(port)
