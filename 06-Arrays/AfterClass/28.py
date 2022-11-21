def median(array):
    n = len(array)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    if n%2 != 0:
        print(array[n//2])
    else:
        print((array[n//2]+array[(n//2)-1])/2)
median([1,0,9,4,6])
median([6,8,3,1,0,5,7])
median([3,1,6,1,12,9])