# file-server

**Category**: web

**Points**: 300

i just wanted a good file hosting service man

http://195.154.231.70:1337/

## Files

- [file-server.zip](./file-server.zip)

## Solution

the vulnerability is in the unzip function, you can upload a zip with a symlink to `/tmp/flag.txt` (location found in the Dockerfile) and get the flag.

to generate the zip to be uploaded, simply use `ln -s /tmp/flag.txt exp`, then `zip --symlink exp.zip exp`.

then upload it onto the site, navigate to your unique UUID, and append `/exp` to it to get a file containing the flag.
