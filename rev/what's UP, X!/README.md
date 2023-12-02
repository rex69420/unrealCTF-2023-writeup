# what's UP, X!

**Category**: rev

**Points**: 200

something funny about the question title..

## Files

- [chall](./chall)

## Solution

the binary is compiled with upx. decompile it using upx with `upx -d chall` and open it in ghidra.

![ghidra](https://i.imgur.com/0bbHPJf.png)

see that the input is being compared to `6942` and if it's correct, it will print the flag.

simply input `6942` and get the flag.

![flag](https://i.imgur.com/xOJQQtL.png)
