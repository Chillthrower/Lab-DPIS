from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

k = get_random_bytes(16)
b = b'This is a secret message.'

c = AES.new(k, AES.MODE_EAX)
ct, t = c.encrypt_and_digest(b)

c = AES.new(k, AES.MODE_EAX, nonce=c.nonce)
dec = c.decrypt_and_verify(ct, t).decode()

print("Encrypted:", ct)
print("Decrypted:", dec)