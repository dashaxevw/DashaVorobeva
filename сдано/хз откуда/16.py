import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n>=2025: return n
    else: return n+3+f(n+3)
print(f(2018)-f(2022))