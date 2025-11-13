from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util import number

k = RSA.generate(2048)
m = b'This is a secret message.'

ct = PKCS1_OAEP.new(k.publickey()).encrypt(m)
rsa = PKCS1_OAEP.new(k).decrypt(ct).decode()

p = number.getPrime(128)
priv = number.getRandomRange(2, p-2)
ans = pow(2, priv, p)

print("RSA:", rsa)
print("DH public:", ans)