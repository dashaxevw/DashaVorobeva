x=[]
for n in range(1,10000):
    b=bin(n)[2:]
    if int(b)%3==0:
        b='1'+b[:-2]+'11'
    else:
        b='10'+b+'0'
    r=int(b,2)
    if r>999 and n%2!=0:
        x.append(r)
print(min(x))
#я не знаю как исправить(((((