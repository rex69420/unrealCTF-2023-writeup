# sst\_

**Category**: forensics

**Points**: 250

**slow**ly fill in the blank of qname :p

(only use the bottom row of your keyboard)

## Files

- [me_when.jpg](./me_when.jpg)
- [sst.wav](./sst.wav)

## Solution

decode the wav file using a sstv [decoder](https://github.com/colaclanth/sstv), to get this output.

![sstv](https://i.imgur.com/PZpZiKB.png)

then, run binwalk on `me_when.jpg` with the command `binwalk -c -e me_when.jpg` to get back a password locked zip file.

using the password `ch1ck3np0pc0rn` found in the sstv output, we can extract the zip file and get `almost.txt`

this is a base64 encoded image, convert it to a png.

```bash
cat almost.txt | base64 -d > almost.png
```

![almost](https://i.imgur.com/Ms7Omir.png)

head over to https://pastebin.com/t55mARzS which can be clearly seen in the image to get -

```
oh wait wh TVJMVEs2SzJLNURIR1pKU0tKWUZVM0syTlJSVzJWVFZNUkREUzZUREdOSkdNWUtYTEkyV0NNM01PSlRGQ1BKNQ==
```

decode the string from base64, then base32, then base64 again to get the flag. this can be done easily using cyberchef's magic feature.

![cyberchef](https://i.imgur.com/ofkm5F2.png)
