# """
# Orel and reshka problem: how many times we need to fly up a coin to meet 4 times the same side: reshka OR orel.
# """

import random

o = 0
r = 0

coin = {1: "Orel", 2: "Reshka"}
attempts = []

while o < 4 and r < 4:
    choice = random.randint(1, 2)
    attempts.append(coin[choice])
    if choice == 1:
        o += 1
        r = 0
    else:
        r += 1
        o = 0

print(attempts)
print(len(attempts))