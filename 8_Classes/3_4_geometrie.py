import math

class Point :
    
    def __init__ ( self, x=0, y=0 ) :
        self.abscisse = x
        self.ordonnee = y
        
    def affichage ( self ) :
        print ( "Point : (", self.abscisse, ";", self.ordonnee, ")" )
        
    def distance ( self, autrePoint ) :
        deltaX = self.abscisse - autrePoint.abscisse
        deltaY = self.ordonnee - autrePoint.ordonnee
        return math.sqrt ( deltaX * deltaX + deltaY * deltaY )
        
    def translation ( self, vect ) :
        self.abscisse = self.abscisse + vect.dx
        self.ordonnee = self.ordonnee + vect.dy
        
        
class Segment :
    
    def __init__ ( self, A, B ) :
        self.p1 = A
        self.p2 = B 
        
    def affichage ( self ) :
        print ( "***** Segment *****" )
        print ( self.p1.affichage() )
        print ( self.p2.affichage() )
        print ( "*******************" )
        
    def longueur ( self ) :
        return A.distance(B)
        
    def milieu ( self ) :
        x = ( p1.abscisse + p2.abscisse ) / 2
        y = ( p1.ordonnee + p2.ordonnee ) / 2
        return ( Point ( x, y ) )
        
    def translation ( self, vect ) :
        self.p1.translation ( vect )
        self.p2.translation ( vect )
        
class Triangle :

    def __init__ ( self, A, B, C ) :
        self.p1 = A
        self.p2 = B 
        self.p3 = C 
    
    def affichage ( self ) :
        print ( "***** Triangle *****" )
        print ( self.p1.affichage() )
        print ( self.p2.affichage() )
        print ( self.p3.affichage() )
        print ( "********************" )
        
    def estEquilateral ( self ) :
        long1 = self.p1.distance ( self.p2 )
        long2 = self.p2.distance ( self.p3 )
        long3 = self.p3.distance ( self.p1 )
        return long1 == long2 and long2 == long3
        
    def estIsocele ( self ) :
        long1 = self.p1.distance ( self.p2 )
        long2 = self.p2.distance ( self.p3 )
        long3 = self.p3.distance ( self.p1 )
        return long1 == long2 or long2 == long3 or long3 == long1
    
    def estRectangle ( self ) :
        long1 = self.p1.distance ( self.p2 )
        long2 = self.p2.distance ( self.p3 )
        long3 = self.p3.distance ( self.p1 )
        hyp = max ( long1, long2, long3 )
        a = min ( long1, long2, long3 )
        b = long1 + long2 + long3 - hyp - a
        return hyp*hyp == a*a + b*b
        
    def centre_de_gravite ( self ) :
        x = ( p1.abscisse + p2.abscisse + p3.abscisse ) / 3
        y = ( p1.ordonnee + p2.ordonnee + p3.ordonnee ) / 3
        return ( Point ( x, y ) )
              
class Vecteur :

    def __init__ ( self, A, B ) :
        self.dx = B.abscisse - A.abscisse
        self.dy = B.ordonnee - A.ordonnee
        
    def norme ( self ) :
        return math.sqrt ( dx*dx + dy*dy )
    
    def retourne ( self ) :
        self.dx = -self.dx
        self.dy = -self.dy 
        
p1 = Point()
p2 = Point ( 1, 1 )
print ( p1.distance ( p2 ) )


# Avancé : Vecteur : x, y, norme, inverse
# translation rotation ( point, angle ) et scale (ctrer sur le cntre de gravité) et similitude