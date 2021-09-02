def pgcd ( a, b ) :
    # On corrige les inputs s'ils sont négatifs ou dans le mauvais ordre
    if a < 0 :
        a = -a
    if b < 0 :
        b = -b
    if a < b :
        tmp = a
        a = b
        b = tmp
        
    # L'algorithme d'Euclide : calcul du résultat de la division entière puis décalage de variables
    while b > 0 :
        r = a%b
        a = b
        b = r
        
    return a
    
print ( pgcd ( 128, 12 ) )
print ( pgcd ( -9, 15 ) )
print ( pgcd ( -17, -13 ) )

    