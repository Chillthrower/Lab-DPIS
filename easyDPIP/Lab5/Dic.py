import hashlib

def h(pw, s): 
    return hashlib.sha256((s+pw).encode()).hexdigest()

users = {
    "alice": ("S1", h("apple123","S1")),
    "bob":   ("X9", h("qwerty","X9")),
    "carol": ("ZZ", h("letmein","ZZ"))
}

c = ["password","123456","qwerty","apple123","letmein"]

def crack(salt, stored):
    return next((pw for pw in c if h(pw, salt)==stored), None)

for name in ["alice", "bob", "carol"]:
    salt, stored = users[name]
    pw = crack(salt, stored)
    print(f"{name}: {pw}   |   {stored}")