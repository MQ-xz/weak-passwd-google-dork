def encrypt():
	plain=input("Enter plain text to encrypt \n")
	key=int(input("Enter key shift \n"))
	cipher=[]
	for i in plain:
		y=ord(i)                                #converting to ascii value
		y=y+key                                 #adding key to ascii
		z=chr(y)                                #converting ascii to character
		cipher.append(z)
	string=''
	for i in cipher:                                #changing from character array to string
		string=string+i
	print(string)
def decrypt():
	cipher=input("Enter cipher text to decrypt \n")
	key=int(input("Enter key shift \n"))
	plain=[]
	for i in cipher:
		y=ord(i)
		y=y-key
		z=chr(y)
		plain.append(z)
	string=''
	for i in plain:
		string=string+i
	print(string)
def nokey_decrypt():
	cipher=input("Enter cipher text to decrypt \n")
	key=0
	while(key<26):                                      #Bruteforcing every 26 possible keys
		plain=[]
		for j in cipher:
			y=ord(j)
			y=y-key
			z=chr(y)
			plain.append(z)
		string=''
		for i in plain:
			string=string+i
		print(string)
		key=key+1
print("What do you want to do\n")
option=int(input("1-encrypt\n2-decrypt\n"))
if option==1:
	encrypt()
elif option==2:
	que=input("Do you know key (y)es or (n)o?\n")
	if que=='y':
		decrypt()
	elif que=='n':
		nokey_decrypt()
	else:
		print("Please Enter valid option")
else:
	print("Please Enter valid option")
print("****Thank You****")
