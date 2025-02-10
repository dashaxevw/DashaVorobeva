from itertools import *
s=''
c=0
for i in product('012345678',repeat=7):
    s=''.join(i)
    if s[0]!='0' and s[0]!='2' and s[0]!='4' and s[0]!='6':
        if (s[4]!='0' and s[5]!='0' and s[6]!='0') or (s[4]!='1' and s[5]!='1' and s[6]!='1') or (s[4]!='2' and s[5]!='2' and s[6]!='2') or (s[4]!='3' and s[5]!='3' and s[6]!='3') or (s[4]!='4' and s[5]!='4' and s[6]!='4') or (s[4]!='5' and s[5]!='5' and s[6]!='5') or (s[4]!='6' and s[5]!='6' and s[6]!='6') or (s[4]!='7' and s[5]!='7' and s[6]!='7') or (s[4]!='8' and s[5]!='8' and s[6]!='8'):
            c+=1
print(c)