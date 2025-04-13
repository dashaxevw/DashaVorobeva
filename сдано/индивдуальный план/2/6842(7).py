print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(w and((z or y)==(z and x))):
                    print(x,y,z,w)

                    #1!=w   1==x or 1==z

                    #xywz