from itertools import *
s=''
c=0
for i in product('01234567', repeat=7):
    s=''.join(i)
    if (s.count('0')+s.count('2')+s.count('4')+s.count('6'))==2 and ('17' not in s) and ('71' not in s) and ('37' not in s) and ('73' not in s) and ('57' not in s) and ('75' not in s) and ('77' not in s):
        c+=1
print(c)