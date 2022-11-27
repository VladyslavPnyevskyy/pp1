import re

mesage = 'To be, or not to be, that is the question'
vowels = re.findall('[euioa]', mesage)
print(len(vowels))