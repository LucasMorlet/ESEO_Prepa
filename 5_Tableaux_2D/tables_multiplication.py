def tables_multiplication ( m, n ) :
    # Création du tableau 2D vide
    tab = [0] * m
    for i in range ( len(tab) ) :
        tab[i] = [0] * n
        
    # Remplissage
    for i in range ( len(tab) ) :
        for j in range ( len(tab[i]) ) :
            tab[i][j] = (i+1)*(j+1)
                     
    return tab
       
 
tab = tables_multiplication ( 5, 9 )
# Affichage ligne par ligne
for i in range ( len(tab) ) :
    print ( tab[i] )