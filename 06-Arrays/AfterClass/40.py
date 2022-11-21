lst = [[-38, 19], [5,40],[-7,11],[29,16]]
x = None
y = None
rowMax = None
lineMax = None
rowMin = None
lineMin = None

lineCounter = 0
for i in lst:
    for j in i:
        if x == None:
            x = j
        if j < x:
            x = j
for i in lst:
    for j in i:
        if y == None:
            y = j
        if j > y:
            y = j
for line in lst:
    rowCounter = 0
    for row in line:
        if x == row:
            rowMax = rowCounter
            lineMax = lineCounter
        if y == row:
            rowMin = rowCounter
            lineMin = lineCounter
        rowCounter=rowCounter+1
    lineCounter= lineCounter + 1
print(f"min:{y}[{lineMin},{rowMin}]")
print(f"max:{x}[{lineMax},{rowMax}]")