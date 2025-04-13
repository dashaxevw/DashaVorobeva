def f(start, end, s):
    if start>end+3 or 'aaa' in s: return 0
    if start==end and 'aaa' not in s: return 1
    if start<end: return f(start-1,end, s+'a')+f(start+5, end, s+'b')+f(start*2, end, s+'c')
print(f(5,34, ''))