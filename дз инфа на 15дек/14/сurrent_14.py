x=2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
c=0
s=''
while x:
    s+=str(x%9)
    if x%9!=0:
        c+=1
    x//=9
print(c)