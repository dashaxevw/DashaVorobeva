import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n==0: return 0
    if n>0 and n%2==0: return f(n//2)
    if n%2!=0: return 1+f(n-1)
c=0
for n in range(1,501):
    if f(n)==8:
        c+=1
print(c)