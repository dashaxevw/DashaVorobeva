a='1'*45+'2'*45
while '111' in a or '222' in a:
    if '111' in a:
        a=a.replace('111', '2', 1)
    else:
        a=a.replace('222', '1', 1)
print(a)