#!/usr/bin/python
import os
import time
Print "+          [Auto dorking]               +"
Print "+  Author      : security007       +"
Print "+  Last Update : 27-01-2018   +"
Print "+  *Kalau mau ganti author    +"
Print "+  *Buat tool sendiri!!               +"
Print " "
dork = raw_input("Dork : ")
st = raw_input("Jumlah Output (1-100): ")
print "Menerima data dari google"
time.sleep(2)
try:
	os.system("google --tld=com --stop="+st+" --num="+st+" "+dork)
except:
	print "Installing Google Module"
	os.system("pip install google")
	print "Success installing module"
	print "Type python dorker.py and enjoy it"
