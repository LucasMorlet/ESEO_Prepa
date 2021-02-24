def eratosthene ( n ) :
    # Création du tableau de départ
    tab = [True]*n
    tab[0] = False
    tab[1] = False
        
    # Le crible d'Eratosthène
    for i in range ( 2, len(tab) ) :
        # Si le nombre existe encore, il est premier
        if tab[i] == True :
            # On supprime tous ses multiples
            for j in range ( 2*i, len(tab), i ) :
                tab[j] = False
                
    return tab
    
    
tab = eratosthene(100)
for i in range ( len(tab) ) :
    if tab[i] :
        print ( i, end = ", " )