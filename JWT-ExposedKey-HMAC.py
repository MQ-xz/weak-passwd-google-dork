import hmac,hashlib,base64

file = open('/path/key.pem')

key = file.read()

#paste your header and payload here
header = ''
payload = ''

#Creating encoded header
encodedHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodedHeader = str(encodedHBytes, "utf-8").rstrip("=")

#Creating encoded payload
encodedPBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodedPayload = str(encodedPBytes, "utf-8").rstrip("=")

#Concatenating header and payload
token = (encodedHeader + "." + encodedPayload)

#Creating signature
sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"), token.encode('utf-8'),hashlib.sha256).digest()).decode('UTF-8').rstrip("=")

print(token + "." + sig)
