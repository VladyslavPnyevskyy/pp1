def arrFlaten(array):
    result = []
    for i in array:
        result.extend(i)
    array = result
    print(array)
arrFlaten([[2,3],[1,5]])
arrFlaten([[5,0,3,7,5],[9,0,9,1,2]])