lst = [2,1,1,1,1,11,2]
_lst = [0,1,1,1,1,1,1,0]

def chop(lst):
    del lst[0]
    del lst[len(lst)-1]

def midle(lst):
    lst = lst[1:(len(lst)-1)]
    return lst    


