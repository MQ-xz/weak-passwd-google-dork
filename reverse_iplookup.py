#! usr/bin/env python3

#This program has been created by Akshay Ravi(C09Y_C47)

#This is a simple reverse ip lookup
import os
os.system("clear")
banner='''
.____                  __                 
|    |    ____   ____ |  | ____ ________  
|    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
|    |__(  <_> |  <_> )    <|  |  /  |_> >
|_______ \____/ \____/|__|_ \____/|   __/ 
        \/                 \/     |__|    
         #Created By Akshay Ravi
        '''
        
print(banner)
cmd= "curl -s http://api.hackertarget.com/reverseiplookup/?q=" + input("[-]Enter Site Name : ")
print("[-]searching for credentials")
print("[-]Please Wait .... \033[1;33;40m")
os.system(cmd)
exit(1)
