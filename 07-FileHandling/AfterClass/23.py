import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
ssum = []
for i in temperatures:
    i = int(i)
    ssum.append(i)

print(sum(ssum)//len(ssum))
