for i in range ( 100 ) :
    # Si le nombre est pair mais pas multiple de 7
    if i%2 == 0 and i%7 != 0 :
        print ( i, end = ", " )
    # Si le nombre n'est pas pair mais est un multiple de 7
    elif i%2 != 0 and i%7 == 0 :
        print ( i, end = ", " )
    