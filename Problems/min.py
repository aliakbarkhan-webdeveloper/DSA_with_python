li=[22,128,13]
def mini(l):
    if l.__len__()==0:
        return None
    min=0
    max=1
    res=0
    while max<l.__len__():
        if l[min] < l[max]:
            res=l[min]

        else:
            res=l[max]
            min=max
        max+=1
    return res

print(mini(li))