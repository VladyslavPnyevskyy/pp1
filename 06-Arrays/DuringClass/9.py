lst = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
y=""
for name in lst:
    if len(name)>len(y):
        y=name
print(y)