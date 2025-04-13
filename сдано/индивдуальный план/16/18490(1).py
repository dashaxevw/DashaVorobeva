import sys
sys.setrecursionlimit(10**6)

def f(n):
    if n>3000: return n
    if n<=3000: return (2*n+4)*f(n+2)

print(sum(map( int, str ((f(20)//f(28))))))