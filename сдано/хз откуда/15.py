def f(x,a):
    return ((x&52!=0)and(x&36==0))<=(not(x&a==0))
for a in range(0,100):
    if all(f(x,a) for x in range(0,100)):
        print(a)