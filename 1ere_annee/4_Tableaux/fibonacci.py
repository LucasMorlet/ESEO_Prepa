def fibonacci ( n ) :
    # Initialisation du tableau et des deux premières valeurs
    tab = [0] * n
    tab[0] = 0
    tab[1] = 1
    
    # Calcul des nombres de Fibonacci par la formule de récurence 
    for i in range ( 2, len(tab) ) :
        tab[i] = tab[i-1] + tab[i-2]
        
    return tab
    
print ( fibonacci ( 15 ) )