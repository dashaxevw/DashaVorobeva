for n in range(4,10000):
    a='1'+'2'*n
    while '12' in a or '322' in a or '222' in a:
        a=a.replace('12',  '2', 1)
        a=a.replace('322', '21', 1)
        a=a.replace('222', '3', 1)
    if 3*a.count('3')+2*a.count('2')+a.count('1')==15:
        print(n)
        break