

            
def compare(array1, array2):
    counter=0
    if len(array1)==len(array2):
        for i in range(0,len(array1)):
            if array1[i]==array2[i]:
                counter = counter +1
                continue    
            else:
                print(False)
                break
        if counter == len(array1):
            print(True)

    else:
        print(False)
compare(["water","book","sky"] , ["water","book","sky"])
compare([True,False], [True,False,True])
compare([5,3,1],  [5,3,1])
compare([3,2,1],    [3,2])
compare([1,1,1], [1,1,2])