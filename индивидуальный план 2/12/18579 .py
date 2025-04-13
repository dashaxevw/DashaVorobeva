a='>'+'3'*10+'5'*10+10*'7'
while '>3' in a or '>5' in a or '>7' in a:
    if '>3' in a: a=a.replace('>3', '55>', 1)
    if '>5' in a: a=a.replace('>5', '5>3', 1)
    if '>7' in a: a=a.replace('>7', '3>5', 1)
b=7*a.count('7')+5*a.count('5')+3*a.count('3')
print(b)