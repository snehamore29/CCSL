from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)
cipher = DES.new(key, DES.MODE_EAX)
nonce = cipher.nonce

dt = input('Enter a message: ')
ciphertext, tag = cipher.encrypt_and_digest(dt.encode())

print(f'Cipher text: {ciphertext}')
cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print(f'Plain text: {plaintext.decode("ascii")}')

