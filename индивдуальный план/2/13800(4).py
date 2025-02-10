print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x==y)or(y==w) or(w==z))or(x and not(y)):
                    print(w,x,y,z)


                    # xwzy