def pascal ( n ) :
    # Création du tableau en triangle
    tab = [0] * n 
    for i in range ( len(tab) ) :
        tab[i] = [0]*(i+1)
        
    # Première colonne et diagonale
    for i in range ( len(tab) ) :
        tab[i][0] = 1
        tab[i][i] = 1
        
    # Remplissage du reste du triangle
    for i in range ( 2, len(tab) ) :
        for j in range ( 1, len(tab[i])-1 ) :
            tab[i][j] = tab[i-1][j-1] + tab[i-1][j]
            
    return tab
    
tab = pascal ( 10 )
# Affichage ligne par ligne
for i in range ( len(tab) ) :
    for j in range ( len(tab[i]) ) :
        print ( tab[i][j], end = " " )
    print ("")