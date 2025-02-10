x=[]
for n in range(1,10000):
    b=bin(n)[2:]
    if n%2==0:
        b=b+'10'
    else:
        b='1'+b+'01'
    r=int(b,2)
    if r>441:
        x.append(n)
print(min(x))