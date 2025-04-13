s=set()
for  n in range(4,1000):
    a='7'+'6'*n
    while '766' in a or '667'in a:
        if '766' in a: a=a.replace('766', '67', 1)
        if '667' in a: a=a.replace('667', '7', 1)
    s.add(a)
print(s)
print (len(s))