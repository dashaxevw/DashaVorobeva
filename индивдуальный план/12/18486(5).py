c=0
for n in range(4,10000):
    a='7'+n*'6'
    while '766' in a or '667' in a:
        if '766' in a:
            a=a.replace('766', '67',1)
        if '677' in a:
            a=a.replace('677', '7', 1)
            c+=1
print(c)