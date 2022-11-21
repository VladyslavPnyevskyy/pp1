def compare(array1, array2):
    if array1==array2:
        print(True)
    else:
        print(False)
compare(["water","book","sky"] , ["water","book","sky"])
compare([True,False], [True,False,True])
compare([5,3,1],  [5,3,1])
compare([3,2,1],    [1,3,2])
compare([1,1,1], [1,1,2])