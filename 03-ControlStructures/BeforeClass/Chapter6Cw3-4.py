fruit = "banana"
name = "alan"

def count(word):
    counts = 0
    for leter in word:
        if leter == "a":
            counts = counts+1
    print(counts)

count(fruit)
count(name)

#ćw. 4
print(fruit.count("a"))