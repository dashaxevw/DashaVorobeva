for n in range(4,10000):
    a='2'+'5'*n
    while '25' in a or '355' in a or '555' in a:
        a=a.replace('25', '5',1)
        a=a.replace('355', '522', 1)
        a=a.replace('555', '3', 1)
    if a.count('2')==10:
        print(n)
        break