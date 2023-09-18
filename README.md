# far
Find And Replace

# Usage
```bash
python3 far <path> <query> <replace> <-flag>
```
Flags are:

`-e` exact occurrences, uses regex to find exact matches to `query`

`-a` all occurrences, does not use regex to find exact matches to `query`

As an example, if I run with the following:

```bash
python3 far /home/myfiles/dev/python-projects/ def fed -e
```

It will only replace occurrences of the **exact** query _def_ and replace it with _fed_.

However, if I ran with:

```bash
python3 far /home/myfiles/dev/python-projects/ def fed -a
```

It will replace **all** occurrences of the query _def_ and replace it with _fed_. So if you have a word such as _default_, it will be replaced with _fedault_.
