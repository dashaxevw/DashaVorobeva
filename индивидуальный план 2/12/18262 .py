import math
for n in range(1000):
    a='>'+17*'0'+n*'3'+17*'2'
    while '>3' in a or '>2' in a or '>0' in a:
        if '>3' in a: a=a.replace('>3', '22>', 1)
        if '>2' in a:a=a.replace('>2', '2>', 1)
        if '>0' in a: a=a.replace('>0' , '3>', 1)
    b= 3*a.count('3')+2*a.count('2')
    print(n,b)