from Case import *
from random import randrange

class Grille :

    # Constructeur
    def __init__ ( self, w, h, n ) :
        self.largeur = w
        self.hauteur = h
        self.nbBombes = n
        self.genereTableau()
        self.genereBombes()
        self.calculValeursTableau()
        
    # Accesseurs        
    def estUneCaseValide ( self, i, j ) :
        return ( 0 <= i and i < self.hauteur and 0 <= j and j < self.largeur )
        
    def isBombe ( self, i, j ) :
        return self.tableau[i][j].isBombe()
        
    def getNbCasesVisible ( self ) :
        nb = 0
        for i in range ( self.hauteur ) :
            for j in range ( self.largeur ) :
                if ( self.tableau[i][j].isVisible() and not self.tableau[i][j].isBombe() ) :
                    nb += 1
        return nb
        
    # Création de la grille
    def genereTableau ( self ) :
        self.tableau = [0]*self.hauteur
        for i in range ( self.hauteur ) :
            self.tableau[i] = [0]*self.largeur
            for j in range ( self.largeur ) :
                self.tableau[i][j] = Case()
        
    def genereBombes ( self ) :
        n = 0
        while ( n < self.nbBombes ) :
            i = randrange ( self.hauteur )
            j = randrange ( self.largeur ) 
            if ( not self.tableau[i][j].isBombe() ) :
                self.tableau[i][j].devientBombe()
                n += 1
    
    def calculValeursTableau ( self ) :
        for i in range ( self.hauteur ) :
            for j in range ( self.largeur ) :
                if ( not self.tableau[i][j].isBombe() ) :
                    self.calculValeurCase ( i, j )
    
    def calculValeurCase ( self, i, j ) : 
        n = 0
        for u in [ i-1, i, i+1 ] :
            for v in [ j-1, j, j+1 ] :
                if ( u >= 0 and u < self.hauteur and v >= 0 and v < self.largeur ) :
                    if ( self.tableau[u][v].isBombe() ) :
                        n += 1
        self.tableau[i][j].setValeur(n) 
   
    # Méthode de jeu
    def reveleTotalite ( self ) :
        for i in range ( self.hauteur ) :
            for j in range ( self.largeur ) :
                self.tableau[i][j].revele()
    
    def reveleCase ( self, i, j ) :
        if ( self.estUneCaseValide ( i, j ) ) :
            if ( self.tableau[i][j].isVisible() ) :
                print ( "Case deja revelee" )
            elif ( self.tableau[i][j].isDrapeau() ) :
                print ( "Impossible de reveler un drapeau" )
            else :
                self.tableau[i][j].revele()
                if ( not self.tableau[i][j].isBombe() ) :
                    self.traiteCaseNombre ( i, j )

    def traiteCaseNombre ( self, i, j ) :
        if ( self.tableau[i][j].isVide() ) :
            self.reveleAlentours ( i, j ) 
                        
    def reveleAlentours ( self, i, j ) :
        for u in [ i-1, i, i+1 ] :
            for v in [ j-1, j, j+1 ] :
                if ( self.estUneCaseValide ( u, v ) ) :
                    if ( not self.tableau[u][v].isVisible() ) :
                        self.tableau[u][v].revele()
                        self.traiteCaseNombre ( u, v )
        
    def switchDrapeau ( self, i, j ) :
        if ( self.estUneCaseValide ( i, j ) ) :
            if ( self.tableau[i][j].isVisible() ) :
                print ( "Impossible de placer un drapeau sur une case revelee" )
            else :
                self.tableau[i][j].switchDrapeau()
    
    # Affichage
    def afficheConsole ( self ) :
        # Header
        print ( '   |', end = ' ' )
        for j in range ( self.largeur ) :
            print ( chr(ord('A')+j), end =' ' )
        print()
        
        # Barre
        for j in range ( 6 + 2*self.largeur ) :
            print ( '-', end='' )
        print()
        
        # Body
        for i in range ( self.hauteur ) :
            print ( '', i%10, '|', end = ' ' )
            for j in range ( self.largeur ) :
                self.tableau[i][j].afficheConsole()
            print( '|' )
            
        # Footer
        for j in range ( 6 + 2*self.largeur ) :
            print ( '-', end='' )
        print()