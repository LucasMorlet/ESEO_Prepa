from PyQt5.QtWidgets import ( QGraphicsRectItem )

class Arene :

    def __init__ ( self, w, h ) :
        self.largeur = w
        self.hauteur = h
         
    def get_visual_representation ( self ) :
        return QGraphicsRectItem ( 0, 0, self.largeur, self.hauteur )