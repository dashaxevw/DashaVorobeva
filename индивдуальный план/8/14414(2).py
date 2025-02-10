from itertools import *
s=''
c=0
for i in product('012345678', repeat=7):
    s=''.join(i)
    if s[0]!='0' and s.count('6')==1:
        s = s.replace('2', '0')
        s = s.replace('3', '1')
        s = s.replace('4', '0')
        s = s.replace('5', '1')
        s = s.replace('6', '0')
        s = s.replace('7', '1')
        s = s.replace('8', '0')

        if '11' not in s and '00' not in s:
            c+=1
print(c)