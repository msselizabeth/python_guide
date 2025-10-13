import re

text = "la la hey shit - oh FUCK nooo, ofucko stop fucking, bloody hell"
bad_words = ["fuck", "shit", "bloody"]

def replace_bad_word(word):
    return "*" * len(word.group())

def replace_spam_words(text, bad_words):
    pattern = rf"\b({'|'.join(bad_words)})\b|\b({'|'.join(bad_words)})"
    return re.sub(pattern, replace_bad_word, text, flags=re.IGNORECASE)

res = replace_spam_words(text, bad_words)
print(res)

# string = f"{'b' + '|'.join(bad_words)}"
# print(string)

