from Crypto.Cipher import AES
from secrets import token_bytes


key = token_bytes(16) #generate key 
cipher = AES.new(key, AES.MODE_EAX) #creating object
nonce = cipher.nonce
dt=input('Enter the message:')
ciphertext, tag = cipher.encrypt_and_digest(dt.encode()) # converting to cipher text (encrypting)
print("Cipher text:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext) #decrypting
print("Plain text:", plaintext.decode())

