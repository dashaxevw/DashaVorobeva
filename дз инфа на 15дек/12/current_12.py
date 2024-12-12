def f(k):
    sm=0
    for x in k:
        sm+= int(x)
    returm sm

l=[]
for n in range(3,10000):
    a='3'+'5'*n
    while '333' in a or '555' in a:
        if '555' in a:
            a=a.replace('555','3',1)
        else:
            a=a.replace('333','5',1)
    l.append(k(a))
print (max(a))