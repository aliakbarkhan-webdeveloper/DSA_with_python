def dec_to_bin(n):
    s=[]
    if n == 0:
        print("value should be greater than 0")
        return None
    while n!=0:
        rem=n%2
        n=n//2
        s.append(rem)
    ret=''
    while s.__len__()!=0:
        ret += str(s.pop())
    return ret

print(dec_to_bin(0))
