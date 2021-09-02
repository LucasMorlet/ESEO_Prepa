import math

class Complexe :
    
    def __init__ ( self, a=0, b=0 ) :
        self.reelle = a
        self.imaginaire = b
        
    def module ( self ) :
        return math.sqrt ( self.reelle ** 2 + self.imaginaire ** 2 )
        
    def angle ( self ) :
        if ( self.imaginaire >= 0 ) :
            return math.acos ( self.reelle / self.module() )
        else :
            return -math.acos ( self.reelle / self.module() )
            
    def angle_degre ( self ) :
        return ( self.angle()*180 )/3.14159286
            
    def affichage ( self ) :
        print ( "z =", self.reelle, "+", self.imaginaire, "i" )
        print ( "r =", self.module(), "theta =", self.angle_degre() )
        
    def plus ( self, autreComplexe ) :
        self.reelle = self.reelle + autreComplexe.reelle
        self.imaginaire = self.imaginaire + autreComplexe.imaginaire
        
    def moins ( self, autreComplexe ) :
        self.reelle = self.reelle - autreComplexe.reelle
        self.imaginaire = self.imaginaire - autreComplexe.imaginaire
        
    def fois ( self, autreComplexe ) :
        a = self.reelle
        b = self.imaginaire
        a2 = autreComplexe.reelle
        b2 = autreComplexe.imaginaire
        self.reelle = a*a2 - b*b2
        self.imaginaire = a*b2 + a2*b
        
z = Complexe()
z.plus ( Complexe ( 2, 1 ) )
z.moins ( Complexe ( 1, 0 ) )
z.affichage()