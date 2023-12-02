# aes

**Category**: crypto

**Points**: 150

let's see how advanced the advanced encryption system is

## Files

- [chall.py](./chall.py)

the key is only 2 bytes long and paded, so we can bruteforce it.

```python
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad, unpad

key_len = 2
bs = 16
known_text = b"unreal{"

iv = bytes.fromhex("fa538d86568da7582d7b4f73af4be04a")
ct = bytes.fromhex("437170f8040b120360427c8e049d08c1c3a0bc94a3c592e05d79ca84f44369cf")

for i in range(key_len**8, key_len**16): # 2**16 is the maximum value of key_len
    key = pad(long_to_bytes(i), bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)
    if known_text in pt:
        print(f"[+] key: {key.hex()}") # 2f1c0e0e0e0e0e0e0e0e0e0e0e0e0e0e
        print(f"[+] flag: {unpad(pt, bs).decode()}") # unreal{m3_wh3n_/d3v/ur4nd0m}
        break
```
