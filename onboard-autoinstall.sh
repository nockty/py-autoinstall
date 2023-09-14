#!/bin/sh

sblock=$(cat <<EOF
# Enable autoinstall
exec(__import__("inspect").getsource(__import__("sys").modules[__name__])[-567:].replace("# ", ""))
# Your script starts here
EOF
)

eblock=$(cat <<EOF

# Autoinstall helper. Keep this block at the end of the file
# src = __import__("inspect").getsource(__import__("sys").modules[__name__])[147:-627]
# new_src = ""
# for line in src.split("\\\\n"):
#     if not line.startswith("import "):
#         new_src += line + "\\\\n"
#         continue
#     module = line.split(" ")[1]
#     new_src += (
#         "try:\\\\n"
#         "    import {module}\\\\n"
#         "except ModuleNotFoundError:\\\\n"
#         "    __import__('subprocess').call(['pip', 'install', '{module}'])\\\\n"
#         "finally:\\\\n"
#         "    import {module}\\\\n"
#     ).format(module=module)
# exec(new_src)
# exit()

EOF
)

echo "$sblock" | cat - $1 > tmp6438564954 && mv tmp6438564954 $1
echo "$eblock" >> $1
