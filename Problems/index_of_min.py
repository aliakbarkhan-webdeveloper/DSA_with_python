li=[1288,1288,2222]
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
    print("Position:",res+1)
    return (res+1,li[res])

print(mini(li))