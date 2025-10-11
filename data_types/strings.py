'''
Recive the search value from: 
<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>
'''

url = 'https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t'

index_of_sq = url.index("?")
index_of_end_of_sq = url.index("&")
search = url[index_of_sq :index_of_end_of_sq]
print(search)

index_of_equal = search.index("=")
search = search[index_of_equal + 1:].replace("+", " ")

print(search)

