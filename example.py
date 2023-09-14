import time

import requests

print("Querying Google at timestamp {}...\n".format(int(time.time())))

resp = requests.get("https://google.fr")
print("Status: {}".format(resp.status_code))
