import re

mesage = 'To be, or not to be, that is the question'
mesage.rstrip()
m = re.split(" ",mesage)
print(len(m))