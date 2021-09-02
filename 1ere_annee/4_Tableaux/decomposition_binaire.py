# Création d'un tableau à une dimension
# Remplissage d'un tableau par une fonction discrète
# Remplissage d'un tableau par une suite génératrice
# Recherche exhaustive dans un tableau
# Recherche linéaire dans un tableau trié

# Génération d'un tableau des puissances de 2 par la fonction puissance
def genere_puissance_2 ( nb_bits ) :
    tab = [0]*nb_bits
    for i in range ( 0, len(tab) ) :
        tab[i] = 2 ** i
        
    return tab

# Génération d'un tableau des puissances de 2 par multiplications consécutives
def genere_puissance_2_multiplication ( nb_bits ) :
    tab = [0]*nb_bits
    tab[0] = 1
    for i in range ( 1, len(tab) ) :
        tab[i] = tab[i-1] * 2
        
    return tab
 
# Recherche dans le tableau du nombre le plus grand inférieur à une valeur donnée 
#def max_inferieure ( n, puiss ) :
    # val = 0
    # pos = 0
    
    # for i in range ( len(puiss) ) :
        # if val < puiss[i] and puiss[i] <= n :
            # val = puiss[i]
            # pos = i
    
    # return pos

# Idem précédent mais avec un a priori que le tableau est déjà trié    
def puissance_inferieure ( n, puiss ) :
    for i in range ( len(puiss) ) :
        if puiss[i] > n :
            return i-1
    
    return len(puiss) - 1
    
# Décompose un nombre décimal en un tableau de bit de taille donnée (la taille est supposée suffisante)  
def decomposition ( n, nb_bits ) :
    binaire = [0] * nb_bits
    puiss = genere_puissance_2 ( nb_bits )
    while n > 0 :
        i = puissance_inferieure ( n, puiss )
        binaire[i] = 1
        n = n - puiss[i]
        
    return binaire

print()
print ( genere_puissance_2 ( 16 ) )
print ( genere_puissance_2_multiplication ( 16 ) )
print()
print ( " 16 -> 2 ^", puissance_inferieure ( 16, genere_puissance_2(8) ) )
print ( " 19 -> 2 ^", puissance_inferieure ( 19, genere_puissance_2(8) ) )
print ( "  3 -> 2 ^", puissance_inferieure ( 3, genere_puissance_2(8) ) )
print ( "  1 -> 2 ^", puissance_inferieure ( 1, genere_puissance_2(8) ) )
print()
print ( decomposition(17, 8) )
print ( decomposition(63, 8) )  
print ( decomposition(80, 8) ) 
print ( decomposition(2048, 16) ) 
print()