# lobmi

**Category**: forensics

**Points**: 200

love me love me say that you love me

fool me fool me go on and fool me

## Files

- [lobmi.wav](./lobmi.wav)
- [f.pyc](./f.pyc)

decompile the `f.pyc` file to get the code that that was used to encode the flag into the `lobmi.wav` file.

```python
import wave

song = wave.open("orig.wav", mode="rb")
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
string = "unreal{redacted}"
string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * "#"
bits = list(map(int, "".join([bin(ord(i)).lstrip("0b").rjust(8, "0") for i in string])))
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
frame_modified = bytes(frame_bytes)
with wave.open("lobmi.wav", "wb") as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()
```

simply write a script to extract the information `lobmi.wav` file using the same method.

```python
import wave

song = wave.open("lobmi.wav", mode="rb")
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(
    chr(int("".join(map(str, extracted[i : i + 8])), 2))
    for i in range(0, len(extracted), 8)
)
print(string.split("###")[0])

song.close()
```

![flag](https://i.imgur.com/XhG0qL8.png)
