def f(start, end):
    if start<end or start==18: return 0
    if start==end: return 1
    if start>end and start%2==0: return f(start-2, end)+f(start/2,end)
    if start>end and start%2!=0: return f(start-2,end)+f(start-3,end)
print(f(55,3))