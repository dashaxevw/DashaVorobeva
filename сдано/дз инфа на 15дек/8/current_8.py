from itertools import product
a= product('012345678', repeat=5)
c=0
s=''
for i in a:
    s=''.join(i)
    if s.count('5')==1 and s[0]!='0' and ('00' not in s) and ('11' not in s) and ('22' not in s) and ('33' not in s) and ('44' not in s) and ('55' not in s) and ('66' not in s) and ('77' not in s) and ('88' not in s):
        c+=1
print(c)