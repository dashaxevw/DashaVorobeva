from itertools import *
s=''
c=0
for i in product('01234556789abcde', repeat=3):
    s=''.join(i)
    if s[0]>s[1]>s[2]:
        c+=1
for i in product('01234556789abcde', repeat=5):
    s=''.join(i)
    if s[0]>s[1]>s[2]:
        c+=1
print(c)