from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
# Step 1: Key and Data
key = b'8bytekey' # DES key must be exactly 8 bytes
data = b'HelloSymmetricDES'
# Step 2: Padding
padded_data = pad(data, DES.block_size) # Make data length a multiple of 8
# Step 3: Encryption
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(padded_data)
print("Encrypted (Ciphertext):", ciphertext)
# Step 4: Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted_padded = decipher.decrypt(ciphertext)
# Step 5: Unpadding
decrypted = unpad(decrypted_padded, DES.block_size)
print("Decrypted (Plaintext):", decrypted)