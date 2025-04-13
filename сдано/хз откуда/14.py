def f(n):
    s=''
    while n:
        s=str(n%5)+s
        n//=5
    return s
c=[]
for x in range(0,5556):
    a=5**150+5*135-x
    if f(a).count('4')==134:
        #c.append(x)
        print(x)