import sys
sys.setrecursionlimit(10**6)

def f(n):
    if n<10: return n
    if n>=10: return f(n%10)+f(n//10)
c=0
if f(n)==159 and n<2**63:
    c+=1
print(c)

#ЧТО ЭТО ТАКОЕ?? я ничего не поняла((((((