class Case :

    # Constructeurs
    def __init__ ( self ) :
        self.estUneBombe = False
        self.valeur = 0
        self.etat = 'c' # c : cache, d : drapeau, v : visible
        
    # Accesseurs
    def isBombe ( self ) :
        return self.estUneBombe
        
    def isVisible ( self ) :
        return self.etat == 'v' 
        
    def isDrapeau ( self ) :
        return self.etat == 'd' 
        
    def isVide ( self ) :
        return not self.estUneBombe and ( self.valeur == 0 )
        
    # Modifieurs
    def switchDrapeau ( self ) :
        if ( self.etat == 'c' ) :
            self.etat = 'd'
        elif ( self.etat == 'd' ) :
            self.etat = 'c'
            
    def revele ( self ) :
        self.etat = 'v'   
            
    def setValeur ( self, n ) :
        self.valeur = n
        
    def devientBombe ( self ) :
        self.estUneBombe = True  
           
    # Méthodes
    def afficheConsole ( self ) :
        if ( self.etat == 'd' ) :
            print ( '!', end = ' ' )
        elif ( self.etat == 'c' ) :
            print ( '-', end = ' ' )
        elif ( self.estUneBombe ) :
            print ( 'X', end = ' ' ) 
        elif ( self.valeur == 0 ) :
            print ( ' ', end = ' ' ) 
        else :
            print ( self.valeur, end = ' ' )   
