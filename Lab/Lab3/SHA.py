from Crypto.Signature import PKCS1_v1_5 as S
from Crypto.Hash import SHA256 as H
from Crypto.PublicKey import RSA

k = RSA.generate(2048)
m = b'This is a secret message.'

sig = S.new(k).sign(H.new(m))
ans = S.new(k.publickey()).verify(H.new(m), sig)

print("Valid:", ans)
