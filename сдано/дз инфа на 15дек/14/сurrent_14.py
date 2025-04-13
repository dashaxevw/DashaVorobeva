x=6**25+6**15-1296
c=0
s=''
while x:
    s+=str(x%6)
    if x%6!=0:
        c+=1
    x//=6
print(x,c)