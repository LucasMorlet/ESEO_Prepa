def PGCD ( a, b ) :
    if ( a < b ) :
        return PGCD ( b, a )
    elif ( b == 0 ) :
        return a
    else :
        return PGCD ( b, a%b )


class Fraction :

    def __init__ ( self, n = 0, d = 1 ) :
        self.num = n
        self.denom = d
        self.corrige_signe()
      
    def calcul ( self ) :
        return self.num / self.denom
      
    def affiche ( self ) :
        print ( self.num, "/", self.denom, "=", self.calcul() )
        
    def simplifier ( self ) :
        pgcd = PGCD ( abs(self.num), abs(self.denom) )
        self.num = self.num / pgcd
        self.denom = self.denom / pgcd
        
    def egal ( self, autreFraction ) :
        self.simplifier()
        autreFraction.simplifier()
        if ( self.num != autreFraction.num ) :
            return False
        elif ( self.denom != autreFraction.denom ) :
            return False
        else
            return True
            
        
    def corrige_signe ( self ) :
        if ( self.denom < 0 ) :
            self.num = -self.num
            self.denom = -self.denom
        
    def modif_num ( self, n ) :
    
        if isinstance ( n, int ) :
            self.num = n
        else :
            print ( "Erreur : le numérateur doit être un entier" )
            
    def modif_denom ( self, d ) :
    
        if not isinstance ( d, int ) :
            print ( "Erreur : le numérateur doit être un entier" )
            
        elif ( d == 0 ) :
            print ( "Erreur : le dénominateur ne peut pas être nul" )   
        
        else :
            self.denom = d
            self.corrige_signe()
            
        
# Test de création
f = Fraction()
f2 = Fraction ( 8, 12 )
f2.affiche()

# Test sur le numérateur
f2.modif_num ( 6 )
f2.affiche()
f2.modif_num ( "numérateur" )
f2.affiche()
f2.modif_num ( -4 )
f2.affiche()
f2.modif_num ( 4.2 )
f2.affiche()

# Test sur le dénominateur
f2.modif_denom ( "dénominateur" )
f2.affiche()
f2.modif_denom ( 8 )
f2.affiche()
f2.modif_denom ( -4 )
f2.affiche()