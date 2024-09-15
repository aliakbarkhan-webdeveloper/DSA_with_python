li=[222,128,139]
def mini(l):
    if l.__len__()==0:
        return None
    min=0
    max=1
    res=0
    while max<l.__len__():
        if l[min] < l[max]:
            res=min

        else:
            res=max
            min=max
        max+=1
    li[res]=li[-1]
    li.pop()
    return li

print(mini([]))