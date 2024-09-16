def fth(li):
    if len(li) < 3:
        print("li should be minimum of three elements")
        return
    h1=0
    h2=0
    h3=0
    for i in li:
        if i>=h1:
            h3 = h2
            h2=h1
            h1=i
        elif i>=h2:
            h3=h2
            h2=i
        elif i>=h3:
            h3=i
    return h3

print(fth([11,6,2,9,0,5,10,15,14,13]))