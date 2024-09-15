def maxi(li):
    if li.__len__()==0:
        return None
    temp=1
    max=0
    maxi=li[max]
    while temp<li.__len__():
        if li[temp]>li[max]:
            maxi=li[temp]
            max=temp
        temp+=1
    return maxi

print(maxi([]))