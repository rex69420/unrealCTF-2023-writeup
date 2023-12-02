from Crypto.Util.number import bytes_to_long, getPrime

encrypt = b"unreal{redacted}"

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e1, e2 = 32, 94
msg = bytes_to_long(encrypt)
c1 = pow(msg, e1, n)
c2 = pow(msg, e2, n)
print(f"n = {n}, e1 = {e1}, e2 = {e2}, c1 = {c1}, c2 = {c2}")
