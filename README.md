# py-autoinstall

A script to facilitate automatic installation of Python modules.

## Context

A typical Python pattern to not bother installing dependencies before running a script is the following:

```py
try:
    import requests
except ModuleNotFoundError:
    subprocess.call(["pip", "install", "requests"])
finally:
    import requests
```

However, using this pattern for each import is cumbersome. To automate this, you can use the `py-autoinstall` tool.

## Usage

Say you have the following script `example.py`:

```py
import time

import requests

print("Querying Google at timestamp {}...\n".format(int(time.time())))

resp = requests.get("https://google.fr")
print("Status: {}".format(resp.status_code))

```

You run it without installing dependencies and it fails: `ModuleNotFoundError: No module named 'requests'`.

To fix this, you just have to onboard it to `py-autoinstall`:

```sh
./onboard-autoinstall.sh example.py
```

This will edit the script with some helpers. These helpers are actually a block at the beginning of the file and a block at the end. You are free to continue editing your script in between. If you just run it, it will automatically install missing dependencies! Isn't that fantastic?

```
python example.py

Collecting requests
Downloading requests-2.31.0-py3-none-any.whl (62 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 4.2 MB/s eta 0:00:00
(...)
Installing collected packages: requests
Successfully installed requests-2.31.0

Querying Google at timestamp 1694715099...

Status: 200
```

<details>
  <summary>See script with helpers</summary>
  
```py
# Enable autoinstall
exec(__import__("inspect").getsource(__import__("sys").modules[__name__])[-567:].replace("# ", ""))
# Your script starts here
import time

import requests

print("Querying Google at timestamp {}...\n".format(int(time.time())))

resp = requests.get("https://google.fr")
print("Status: {}".format(resp.status_code))

# Autoinstall helper. Keep this block at the end of the file
# src = __import__("inspect").getsource(__import__("sys").modules[__name__])[147:-627]
# new_src = ""
# for line in src.split("\n"):
#     if not line.startswith("import "):
#         new_src += line + "\n"
#         continue
#     module = line.split(" ")[1]
#     new_src += (
#         "try:\n"
#         "    import {module}\n"
#         "except ModuleNotFoundError:\n"
#         "    __import__('subprocess').call(['pip', 'install', '{module}'])\n"
#         "finally:\n"
#         "    import {module}\n"
#     ).format(module=module)
# exec(new_src)
# exit()
```

</details>
