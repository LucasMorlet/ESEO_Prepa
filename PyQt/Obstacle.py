from PyQt5.QtWidgets import ( QGraphicsRectItem )

class Obstacle :

    def __init__ ( self, x, y, w, h ) :
        self.posX = x
        self.posY = y
        self.largeur = w
        self.hauteur = h
         
    def get_visual_representation ( self ) :
        return QGraphicsRectItem ( self.posX, self.posY, self.largeur, self.hauteur )