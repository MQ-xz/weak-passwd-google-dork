import mmh3,requests,codecs,sys,urllib3

urllib3.disable_warnings()

if len(sys.argv) == 1:
	print("[!]Please provide a valid URL, If you are facing some issue please add http:// or https:// befor the url")
	print("[+]Example: python3 Hash.py https://www.google.com/favicon.ico")
	exit()

response =requests.get(sys.argv[1], verify=False)
favicon = codecs.encode(response.content,'base64')
hash= mmh3.hash(favicon)
print('[+]shodan search query: http.favicon.hash:'+str(hash))
