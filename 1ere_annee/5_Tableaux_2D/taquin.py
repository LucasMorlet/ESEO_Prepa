from random import *

def genere_taquin ( nb_lignes, nb_colonnes ) :
    taquin = [0]*nb_lignes
    for i in range ( len ( taquin ) ) :
        taquin[i] = [0]*nb_colonnes
     
    ligne_courante = 0
    case_courante = 0 
    for i in range ( 1, nb_lignes*nb_colonnes ) :
        taquin[ligne_courante][case_courante] = i
        case_courante += 1
        if ( case_courante >=nb_colonnes ) :
            case_courante = 0
            ligne_courante += 1
    
    taquin[ nb_lignes-1 ][ nb_colonnes-1 ] = ' '
    return taquin
    
def trouve_trou ( taquin ) :
    for i in range ( len ( taquin ) ) :
        for j in range ( len ( taquin[0] ) ) :
            if ( taquin[i][j] == ' ' ) :
                return i*len ( taquin[0] ) + j
    
def droite ( taquin ) :
    pos = trouve_trou ( taquin )
    trouI = pos // len ( taquin[0] )
    trouJ = pos % len ( taquin[0] )
    if ( trouJ < len ( taquin[0] ) - 1 ) :
        taquin[trouI][trouJ] = taquin[trouI][trouJ+1]
        taquin[trouI][trouJ+1] = ' '
        
    return taquin
        
def gauche ( taquin ) :
    pos = trouve_trou ( taquin )
    trouI = pos // len ( taquin[0] )
    trouJ = pos % len ( taquin[0] )
    if ( trouJ > 0 )  :
        taquin[trouI][trouJ] = taquin[trouI][trouJ-1]
        taquin[trouI][trouJ-1] = ' '
        
    return taquin
        
def bas ( taquin ) :
    pos = trouve_trou ( taquin )
    trouI = pos // len ( taquin[0] )
    trouJ = pos % len ( taquin[0] )
    if ( trouI < len ( taquin ) - 1 )  :
        taquin[trouI][trouJ] = taquin[trouI+1][trouJ]
        taquin[trouI+1][trouJ] = ' '
        
    return taquin
        
def haut ( taquin ) :
    pos = trouve_trou ( taquin )
    trouI = pos // len ( taquin[0] )
    trouJ = pos % len ( taquin[0] )
    if ( trouI > 0 )  :
        taquin[trouI][trouJ] = taquin[trouI-1][trouJ]
        taquin[trouI-1][trouJ] = ' '
        
    return taquin
    
def melange_taquin ( taquin ) :
    for n in range ( 200 ) :
        r = random()*4
        if r < 1 :
            taquin = gauche( taquin )
        elif r < 2 :
            taquin = droite( taquin )
        elif r < 3 :
            taquin = haut( taquin )
        else :
            taquin = bas( taquin )
    
    return taquin
     
def affiche_taquin ( taquin ) :  
    print()
    for i in range ( len ( taquin ) ) :
        print( taquin[i] )
    print()
    
def victoire ( taq, sol ) :
    for i in range ( len ( taq ) ) : 
        for j in range ( len ( taq[0] ) ) :  
            if ( taq[i][j] != sol[i][j] ) :
                return False            
    return True

l = 3
c = 3
sol = genere_taquin ( l, c )
affiche_taquin ( sol )
taq = genere_taquin ( l, c )
taq = melange_taquin ( taq )
affiche_taquin ( taq )
while ( victoire ( taq, sol ) == False ) :
    c = input ( "Où voulez-vous allez ? (z, q, s, d)" )
    if ( c == 'Z' or c == 'z' ) :
        taq = haut(taq)
    elif ( c == 'Q' or c == 'q' ) :
        taq = gauche(taq)
    elif ( c == 'S' or c == 's' ) :
        taq = bas(taq)
    elif ( c == 'D' or c == 'd' ) :
        taq = droite(taq)
    affiche_taquin ( taq )
    
print ()
print ( "******************" )
print ( "*** Victoire ! ***" )
print ( "******************" )
print ()   