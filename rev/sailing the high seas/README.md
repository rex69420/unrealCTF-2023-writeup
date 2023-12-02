# sailing the high seas

**Category**: rev

**Points**: 250

did you know ghidra has a dark theme?

## Files

- [chall](./chall)

## Solution

hint was posted in the discord server: `what do people who sail the seas wear on their eyes?`

this is a reference to eye patches, so we can assume that we have to patch the binary.

![ghidra](https://i.imgur.com/MHAuVG5.png)

opening it up in ghidra, we see that the current time is being compared to `0x7c72bdf9` or `2087894521` which is `Friday, 29 February 2036 10:42:01`

so, we can simply patch this instruction by changing the `JLE` (jump if less than or equal) to a `JGE` (jump if greater than or equal) and exporting it as a binary ("original file" in ghidra).

![before](https://i.imgur.com/QhdEPBa.png)

![after](https://i.imgur.com/V4fYZVJ.png)

after this, we can simply run it and we get the flag.

![flag](https://i.imgur.com/XvDyGxc.png)
