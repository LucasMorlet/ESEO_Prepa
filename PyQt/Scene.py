from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer)
from random import random
from Personnage import *
from Obstacle import *
from Arene import *
import time

class Scene :

    def __init__ ( self ) :
        self.init_static_elements()
        self.init_dynamic_elements()
        self.init_timer()
        
    def init_timer ( self ) :
        self.timer = QTimer()
        self.timer.setInterval ( int(1000/60) )
        self.timer.timeout.connect ( self.deplace_ennemi )
        self.timer.start()
    
    def init_static_elements ( self ) :        
        self.arene = Arene ( 500, 500 )
        self.les_obstacles = []
        self.les_obstacles.append ( Obstacle ( 200, 40, 20, 100 ) )
        self.les_obstacles.append ( Obstacle ( 200, 360, 20, 100 ) )
        self.les_obstacles.append ( Obstacle ( 280, 40, 20, 100 ) )
        self.les_obstacles.append ( Obstacle ( 280, 360, 20, 100 ) )
        self.les_obstacles.append ( Obstacle ( 200, 200, 100, 100 ) )
        self.les_obstacles.append ( Obstacle ( 0, 400, 100, 100 ) )
        self.les_obstacles.append ( Obstacle ( 400, 0, 100, 100 ) )
        
    def init_dynamic_elements ( self ) :
        
        self.personnage = Personnage ( 100, 100, 10 )
        self.ennemi = Personnage ( 400, 400, 2 )
     
    def deplace_perso ( self, dx, dy ) :
        self.personnage.deplace ( dx, dy, self.arene, self.les_obstacles )
        
    def deplace_ennemi ( self ) :
        self.ennemi.deplace_aleatoirement( self.arene, self.les_obstacles )
    
