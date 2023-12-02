import base64
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from dotenv import load_dotenv

load_dotenv()
flag = os.getenv("FLAG")

length = "Mg=="
bs = 16

key = pad(open("/dev/urandom", "rb").read(int(base64.b64decode(length))), bs)
iv = open("/dev/urandom", "rb").read(bs)

cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(flag.encode("utf-8"), 16))

print(f"[+] iv = {iv.hex()}")
print(f"[+] ct = {ct.hex()}")

# stdout ->
# [+] iv = 7d71bf6a2f1393c07a330fc54baae70a
# [+] ct = d244c13293d94356cdb70ad01c5fe8977e2e5feb43d9cb3b9bb9cea648bdabc6
