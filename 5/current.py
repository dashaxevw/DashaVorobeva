for n in range(1,1000):
    b=bin(n)[2:]
    d=str(b.count('1')%2)
    c=str(b.count('1'))+d
    r=int(c,2)
    if r>97:
        print(r)