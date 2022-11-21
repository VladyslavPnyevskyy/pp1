def bubblesort(array):
    n = len(array)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)
bubblesort([3,2,1])
bubblesort([49,73,22,1,0,9])
bubblesort([6,3,9,0,39,11,3])