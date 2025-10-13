import re

'''
Find all consistencies of vowels 
'''
text = "aebdfbiuweebyyyy wqfrewoifheefd huigaaaopogrjvordfghv"
res = re.findall(r"[aeiou]+", text)

print(res) #['ae', 'iu', 'ee', 'e', 'oi', 'ee', 'ui', 'aaao', 'o', 'o']
