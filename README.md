# Secure pass

This repo contains a couple of scripts that can encrypt and decrypt either single strings or files.
Only csv files are supported so far.

There are four scripts:
* `encrypt.sh` encrypts a single string
* `decrypt.sh` decrypts a single string
* `file_encryption.sh` encrypts a csv file. It takes two arguments, an input and an output file.
* `file_decryption.sh` decrypts a previously encrypted csv file. It takes again two arguments, an input and an output file.

__Note:__ with Python 3.8 there is deprecation of module time imported from simple-crypt.

You may see the following error:
```
...
.../secure-pass/venv/lib/python3.8/site-packages/Crypto/Random/_UserFriendlyRNG.py", line 77, in collect
    t = time.clock()
AttributeError: module 'time' has no attribute 'clock'
```

Until this error is fixed, you can go to the `site-packages` where you have installed the package and edit file `_UserFriendlyRNG.py`.
In line 77 find `t = time.clock()` and change it to `t = time.time()`

This will fix the issue for the time being until you need to reinstall it with the official fix.
