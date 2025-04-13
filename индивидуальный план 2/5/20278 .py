s=[]
for n in range(1,10000):
    b=bin(n)[2:]
    if int(b)%2==0:
        b='101'+b[3:]+'01'
    else:
        b='111'+b[3:]+'10'
    r=int(b,2)
    if r<385:
        s.append(n)
print(max(s))