str = 'HackerRank.com presents "Pythonist 2".'
str1 = ""

print(''.join([i.lower() if i.isupper() else i.upper() for i in str]))