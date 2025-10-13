import re

text = "I love Python"

print(re.search(r"Python", text)) #yes
print(re.match(r"Python", text)) # None (because match look at the begining)