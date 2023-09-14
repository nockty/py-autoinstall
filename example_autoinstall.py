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
