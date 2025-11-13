from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Generate RSA key pair (public + private keys)
key = RSA.generate(2048)

# Function to sign a message with private key
def sign_message(message, private_key):
    # Create SHA-256 hash of the message
    h = SHA256.new(message)
    # Create signer object with private key
    signer = PKCS1_v1_5.new(private_key)
    # Generate digital signature
    signature = signer.sign(h)
    return signature

# Function to verify a digital signature with public key
def verify_signature(message, signature, public_key):
    # Recompute SHA-256 hash of the original message
    h = SHA256.new(message)
    # Create verifier object with public key
    verifier = PKCS1_v1_5.new(public_key)
    # Verify signature against the hash
    return verifier.verify(h, signature)

# ---------------- Example Usage ----------------
message = b'This is a secret message.'

# Sign the message using the private key
signature = sign_message(message, key)

# Verify the signature using the public key
is_valid = verify_signature(message, signature, key.publickey())

print("Is signature valid?", is_valid)
