# secweb

**Category**: web

**Points**: 250

yes another one, go

http://195.154.231.70:5341

## Files

- [sec.zip](./sec.zip)

## Solution

the vulnerability is on line 78, where it attempts to use `os.path.join` at the `/file/<id>` route.

by looking at the Dockerfile, we can see the flag is at `/flag`.

from the docs for `os.path.join`:

`If a component is an absolute path, all previous components are thrown away and joining continues from the absolute path component.`

so, simply uploading a file called `flag` and intercepting the request with burp, we can change the filename to `/flag` and get the flag.

![before](https://i.imgur.com/hthwWH9.png)

![after](https://i.imgur.com/VhD4ZBs.png)

![flag](https://i.imgur.com/cjMaCy4.png)
