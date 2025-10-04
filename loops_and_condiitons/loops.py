# Search for max and min elements
nums = [1,34,2,12,13, -8, 14,15]
max = 0
min = 0

# MAX
for n in nums:
    if n > max:
        max = n
print(f"The max number: {max}")

# MIN
for n in nums:
    if n< min:
        min = n      
print(f"The min number: {min}")


pool = 1000
quantity = 3
try:
    chunk = round((pool / quantity), 2)
    print(chunk)
except ZeroDivisionError:
    print('Divide by zero is not possible!')


