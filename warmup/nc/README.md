# nc

**Category**: warmup

**Points**: 50

this is why i had you guys install ncat

`nc 195.154.231.70 9000`

## Solution

simply connect to it using nc, and you get a linux shell.

you can use `ls` to list the files, and you will find a `flag.txt`

use `cat flag.txt` to get jsfuck output. use an online decoder such as https://enkhee-osiris.github.io/Decoder-JSFuck/ to decode it.

on decoding it, you get brainfuck. to decode that, use a website such as https://www.dcode.fr/brainfuck-language and you'll get the flag.
