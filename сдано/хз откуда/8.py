from itertools import *
c=0
s=''
for x in product('0123456789abcd', repeat=5):
    s=''.join(x)
    if s[0]!='0' and (s[-1]=='0' or s[-1]==3) 