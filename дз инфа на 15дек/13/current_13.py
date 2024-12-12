c=0
for i in range(16):
    b=bin(i)[2:]
    if (b.count('1')+8)%2!=0:
        c+=1
print(c)