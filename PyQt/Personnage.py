from random import random
from PyQt5.QtWidgets import ( QGraphicsEllipseItem )

class Personnage :

    def __init__ ( self, x, y, v ) :
        self.posX = x
        self.posY = y
        self.taille = 20
        self.vitesse = v
        
    def deplace ( self, dx, dy, arene, obstacles ) :
        new_x = self.posX + dx*self.vitesse
        new_y = self.posY + dy*self.vitesse
        if ( self.position_possible ( new_x, new_y, arene, obstacles ) ) :
            self.posX = new_x
            self.posY = new_y
        
    def deplace_aleatoirement ( self, arene, obstacles ) :
        self.deplace ( round( random()*2 - 1 ), round( random()*2 - 1 ), arene, obstacles )
        
    def position_possible ( self, x, y, arene, obstacles ) :
        # Ne sort pas de l'arène
        if ( x-self.taille/2 < 0 or x + self.taille/2 > arene.largeur ) :
            return False
        if ( y - self.taille/2 < 0 or y + self.taille/2 > arene.hauteur ) :
            return False
            
        # Ne percute pas les obstacles
        for i in range ( len ( obstacles ) ) :
            if ( self.collision ( x, y, obstacles[i] ) ) :
                return False
    
        return True
        
    def collision ( self, x, y, obstacle ) :
        collisionX = False
        collisionY = False
        # Test en X
        if ( obstacle.posX < x-self.taille/2 < obstacle.posX + obstacle.largeur ) :
            collisionX = True
        elif ( obstacle.posX < x+self.taille/2 < obstacle.posX + obstacle.largeur ) :
            collisionX = True
        # Test en Y 
        if ( obstacle.posY < y-self.taille/2 < obstacle.posY + obstacle.hauteur ) :
            collisionY = True
        elif ( obstacle.posY < y+self.taille/2 < obstacle.posY + obstacle.hauteur ) :
            collisionY = True
        # Conclusion
        return collisionX and collisionY
        
    def get_visual_representation ( self ) :
        x = self.posX - self.taille/2
        y = self.posY - self.taille/2
        return QGraphicsEllipseItem ( x, y, self.taille, self.taille )