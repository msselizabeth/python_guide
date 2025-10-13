# BH 1959 OE
import random

letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

l1 = random.choices(letters, k=2)
l2 = random.choices(digits, k=4)
l3 = random.choices(letters, k=2)

print(f"l1: {l1}")
print(f"l2: {l2}")
print(f"l3: {l3}")

print(f"{"".join(l1)} {"".join(l2)} {"".join(l3)}")