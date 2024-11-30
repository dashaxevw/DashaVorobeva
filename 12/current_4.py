for n in range(3,100):
    a='3'+'5'*n
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a=a.replace('25','1',1)
        if '355' in a:
            a=a.replace('355', '52', 1)
        if '555' in a:
            a=a.replace('555','23',1)
        if 2*a.count('2')+3*a.count('3')+5*a.count('5')==27:
            print(a,n)
