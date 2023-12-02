# go rev

**Category**: rev

**Points**: 400

pfft

## Files

- [gorev](./gorev)

## Solution

the intended solution was to open it in ghidra, and figure out that the bytes of the flag are being xored with 0x69, and then xor it again with 0x69 to get the flag.

but since no one solved it the intended way, i'll be talking about the unintended and much simpler way, which was to patch the binary.

![ghidra](https://i.imgur.com/FfvrMm3.png)

opening it in ghidra, you can see the `doGoofyShit()` function is called but just above that there is a call to `os.Exit()` which exits the program before the function is called.

you can patch the binary and change the exit call to simply call the function instead.

![before](https://i.imgur.com/1VOad2b.png)

![after](https://i.imgur.com/AwdaQQG.png)

after this, simply export the binary, and run it, to get the flag

![flag](https://i.imgur.com/LAwnXJx.png)
