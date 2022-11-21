lst=[-15, 8, -31, 47, -2, 19]
def maxx(lst):
    x=0
    for i in lst:
        if i>x:
            x=i
    print(x)

def minn(lst):
    x=0
    for i in lst:
        if i<x:
            x=i
    print(x)
maxx(lst)
minn(lst)
    