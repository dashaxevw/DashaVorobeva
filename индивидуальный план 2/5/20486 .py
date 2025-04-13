s=[]
for n in range(4,10000):
    b=bin(n)[2:]
    if n%2==0:
        b=b+b[:3]
    else:
        b='1'+b+'01'
    r=int(b,2)
    if r>600:
        s.append(r)
print(min(s))