from random import random

class Skyjo :

    def __init__ ( self, n ) :
        self.tab = [0]*n
        self.nb_lignes = n
        self.nb_colonnes = n
        
        for i in range ( n ) :
            self.tab[i] = [0]*n
            
        for i in range ( n ) :
            for j in range ( n ) :
                self.tab[i][j] = int ( n*random() ) 
           
    def affiche_tab ( self ) :
        print()
        for i in range ( self.nb_lignes ) :
            print ( " ", end="" )
            for j in range ( self.nb_colonnes ) :
                print ( self.tab[i][j], end = " " )
            print()
        print()
    
    def modif_tab ( self, l, c, r ) :
    
        if ( l < 0 or l >= self.nb_lignes ) :
            print ( "Erreur dans le numéro de ligne" )
            return False
            
        if ( c < 0 or c >= self.nb_colonnes ) :
            print ( "Erreur dans le numéro de colonne" )
            return False
            
        self.tab[l][c] = r
        self.reduire_tableau()
        return True
    
    def verif_ligne ( self ) :
        for i in range ( self.nb_lignes ) :
            b = True
            for j in range ( 1, self.nb_colonnes ) :
                if ( self.tab[i][j] != self.tab[i][0] ) :
                    b = False
                    break
            if ( b == True ) :
                return i
        return -1
        
    def verif_colonne ( self ) :
        for j in range ( self.nb_colonnes ) :
            b = True
            for i in range ( 1, self.nb_lignes ) :
                if ( self.tab[i][j] != self.tab[0][j] ) :
                    b = False
                    break
            if ( b == True ) :
                return j
        return -1

    def detruire_ligne ( self, l ) :
    
        for i in range ( l, self.nb_lignes-1 ) :
            for j in range ( self.nb_colonnes ) :
                self.tab[i][j] = self.tab[i+1][j]
                
        self.nb_lignes -= 1

    def detruire_colonne ( self, c ) :
    
        for i in range ( self.nb_lignes ) :
            for j in range ( c, self.nb_colonnes-1 ) :
                self.tab[i][j] = self.tab[i][j+1]
                
        self.nb_colonnes -= 1
        
    def estFini ( self ) :
        if self.nb_lignes <= 0 :
            return True
        elif self.nb_colonnes <= 0 :
            return True
        else :
            return False
            
    def reduire_tableau ( self ) :
        modif = True
        while ( modif ) :
            modif = False
            
            l = self.verif_ligne()
            if ( l >= 0 ) :
                self.detruire_ligne ( l )
                modif = True
                
            if ( self.estFini() ) :
                break
                
            c = self.verif_colonne()
            if ( c >= 0 ) :
                self.detruire_colonne ( c )
                modif = True
                
            if ( self.estFini() ) :
                break        
    
def joue ( n ) : 
    sky = Skyjo ( n )
    nb_coups = 0
    while ( not sky.estFini() ) :
        
        # On affiche le tableau
        sky.affiche_tab()
        
        # On place la nouvelle carte
        r = int ( random()*n )
        ok = False
        while ( not ok ) :
            print ( "Où voulez-vous placer", r, "?" )
            l = int ( input ( "Ligne : " ) )
            c = int ( input ( "Colonne : " ) )
            ok = sky.modif_tab ( l, c, r )
            
        nb_coups += 1
      
    print()
    print ( "Victoire en", nb_coups, "coups" )
             
joue(4)