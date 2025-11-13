import hashlib

h = lambda pw, s: hashlib.sha256((s + pw).encode()).hexdigest()

users = {
    "alice": ("S1", h("apple123", "S1")),
    "bob":   ("X9", h("qwerty",   "X9")),
    "carol": ("ZZ", h("letmein",  "ZZ")),
}

candidates = ["password", "123456", "qwerty", "apple123", "letmein"]

print("Stored hashes:")
for u, (s, hs) in users.items():
    print(f" {u}: {hs[:12]}...")

print("\nCracking:")
for u, (s, hs) in users.items():
    cracked = next((pw for pw in candidates if h(pw, s) == hs), None)
    print(f"[ATTACKER] {'Cracked ' + u + ' -> ' + cracked if cracked else 'NOT cracked ' + u}")