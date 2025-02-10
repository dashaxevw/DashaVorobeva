

for n in range(1,10000):
    b=bin(n)[2:]
    b=b.replace('0','*')
    b=b.replace('1','0')
    b=b.replace('*','1')
    b=b+'1'
    