import re

log = "Bot act: 192.16.4.162 192.16.4.343 looks blah blh"

# ip
# 0-255.0-255.0-255.0-255

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
res = re.findall(pattern, log)

print(res)