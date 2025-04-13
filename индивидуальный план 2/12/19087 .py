for n in range(4,10000):
    a='2'+'7'*n
    while '27' in a or '777' in a or '377' in a:
        a=a.replace('27', '7', 1)
        a=a.replace('777', '3', 1)
        a=a.replace('377', '72', 1)
    b=(7*a.count('7')+3*a.count('3')+2*a.count('2')+a.count('1'))
    if b%3==0 and b%10==1:
        print(n)