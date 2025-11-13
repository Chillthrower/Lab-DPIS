#!/usr/bin/env python3
# attacker_dict.py - tiny dictionary attack demo (no network)
import hashlib

def h(password, salt):
    return hashlib.sha256((salt + password).encode()).hexdigest()

users = {
    "alice": ("S1", h("apple123", "S1")),
    "bob":   ("X9", h("qwerty", "X9")),
    "carol": ("ZZ", h("letmein", "ZZ")),
}

print("Stored (salt,hash) samples (truncated):")
for u, (s, hs) in users.items():
    print(" ", u, s, hs[:12] + "...")

small_dict = ["password", "123456", "qwerty", "apple123", "letmein"]
print("\nAttacker tries small dictionary...")
for u, (s, target) in users.items():
    cracked = None
    for w in small_dict:
        if h(w, s) == target:
            cracked = w
            break
    if cracked:
        print("[ATTACKER] Cracked", u, "->", cracked)
    else:
        print("[ATTACKER] NOT cracked", u)

print("\nNote: Use bcrypt/argon2 in real systems; this demo uses fast SHA-256 for simplicity.")

