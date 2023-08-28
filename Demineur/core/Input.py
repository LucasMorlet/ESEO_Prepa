class Input :

    def __init__ ( self ) :
        self.erreur = False
        self.caseI = 0
        self.caseJ = 0
        self.action = 'r' # r : revele, d : drapeau
        
    def isErreur ( self ) :
        return self.erreur
    
    def getAction ( self ) :
        return self.action
        
    def getCaseI ( self ) :
        return self.caseI
        
    def getCaseJ ( self ) :
        return self.caseJ

    def traiteString ( self, string ) :
    
        self.erreur = False
    
        # Verification de la taille de l'input
        if ( len(string) < 2 ) :
            print ( "Pas assez de caractere !" )
            self.erreur = True
            return
    
        # Check s'il s'agit d'un drapeau
        if ( string[0] == '!' ) :
            self.action = 'd'
            string = string[1:]
        else :
            self.action = 'r'
        
        # Extraction de la lettre
        lettre = string[0]
        string = string[1:]  
        if ( 'a' <= lettre and lettre <= 'z' ) :
            self.caseJ = ord(lettre) - ord('a') 
        elif ( 'A' <= lettre and lettre <= 'Z' ) :
            self.caseJ = ord(lettre) - ord('A')
        else :
            print ( "Erreur dans la lettre !" )
            self.erreur = True
            return   
        
        # Extraction du nombre 
        if ( string.isdigit() ) :
            self.caseI = int(string)
        else :
            print ( "Erreur dans le nombre" )
            self.erreur = True
            return
