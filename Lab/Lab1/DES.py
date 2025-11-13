from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

k =b'8bytekey'
b = b'HelloSymmetricDES'

ct = DES.new(k, DES.MODE_ECB).encrypt(pad(b, 8))
dec = unpad(DES.new(k, DES.MODE_ECB).decrypt(ct), 8)

print("Encrypted:", ct)
print("Decrypted:", dec)