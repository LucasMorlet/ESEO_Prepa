# Debut de la classe Test
class Test :
    
    # Constructeur
    def __init__ ( self, n=0, d=0.0, s="..." ) :
    
        if isinstance ( n, int ) :
            self.entier = n
        else :
            self.entier = 0
            
        if isinstance ( d, float ) :
            self.decimal = d
        else :
            self.decimal = 0.0  
            
        if isinstance ( s, str ) :
            self.chaine = s
        else :
            self.chaine = "..."
        
    # Affichage
    def affichage ( self ) :
        print ( "*********" )
        print ( "    ", self.entier )
        print ( "    ", self.decimal )
        print ( "    ", self.chaine )
        print ( "**********" )
        print ( )
    
# Fin de la classe Test 

print ( isinstance ( 4, int ) )
print ( isinstance ( 4.2, int ) ) 
    
# Création d'un objet avec des valeurs spécifiques
t2 = Test( 17, 4.2, "bye!" )
print ( "*** Objet avec valeurs spécifiques ***" )
print ( t2.entier )
print ( t2.decimal )
print ( t2.chaine )
print ()

# Création d'un objet "par défaut"
t = Test()
print ( "*** Objet par défaut ***" )
print ( t.entier )
print ( t.decimal )
print ( t.chaine ) 
print ()

# Création d'un objet "bugué"
t3 = Test ( 1, 2.2, 7 )
print ( "*** Objet bugué ***" )
print ( t3.entier )
print ( t3.decimal )
print ( t3.chaine ) 
print ()

# Utilisation des méthodes d'affichage
print ( "*** Affichage par méthode ***" )
t.affichage()
t2.affichage()
t3.affichage()
print()
