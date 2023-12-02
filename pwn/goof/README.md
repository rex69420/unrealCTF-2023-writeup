# goof

**Category**: pwn

**Points**: 200

math time

`nc 195.154.231.70 2000`

## Solution

write a python script to solve the math problem, and send the answer to the server.

```python
from pwn import *

p = remote("195.154.231.70", 2000)

while True:
    p.recvline()
    expr = p.recvline().decode("utf-8").replace("\n", "").replace(" = ?", "")  # extract just the expression
    try:
        ans = eval(expr)
        p.sendline(str(ans).encode("utf-8"))
        log.info("sent: {}".format(ans))
    except:
        log.success(f"flag: {expr}")  # if the expression is invalid, we have the flag
        break
```
