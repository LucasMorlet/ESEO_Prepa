from Scene import *

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QObject, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QPainter,QPen,QFont)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                                QGraphicsLineItem, QGraphicsEllipseItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QLabel, QLineEdit, QPushButton,QWidget, QMainWindow)
                             
                             
                             
class GraphicsScene ( QGraphicsScene ) :

    def __init__ ( self, scene ) :
        QGraphicsScene.__init__ ( self )
        self.scene = scene
        self.init_static_elements()
        self.init_dynamic_elements()
        self.init_timer()
        
    def init_timer ( self ) :
        self.timer = QTimer()
        self.timer.setInterval ( int(1000/60) )
        self.timer.timeout.connect ( self.reset_dynamic_elements )
        self.timer.start()
           
    def init_static_elements ( self ) :  
        self.addItem ( self.scene.arene.get_visual_representation() )
        for i in range ( len ( self.scene.les_obstacles ) ) :   
            self.addItem ( self.scene.les_obstacles[i].get_visual_representation() )  
    
    def init_dynamic_elements ( self ) :  
        self.ellipse_personnage = self.scene.personnage.get_visual_representation()
        self.ellipse_ennemi = self.scene.ennemi.get_visual_representation()
        self.addItem ( self.ellipse_personnage )
        self.addItem ( self.ellipse_ennemi )
        
    def reset_dynamic_elements ( self ) :       
        self.removeItem ( self.ellipse_personnage )
        self.removeItem ( self.ellipse_ennemi )
        self.init_dynamic_elements()
        self.update()
        
    def keyPressEvent ( self, event ) :
        dx = 0
        dy = 0
        #print ( event.key() )
        if ( event.key() == Qt.Key_Z ) :
            dy -= 1
        if ( event.key() == Qt.Key_Q ) :
            dx -= 1
        if ( event.key() == Qt.Key_S ) :
            dy += 1
        if ( event.key() == Qt.Key_D ) :
            dx += 1
            
        self.scene.deplace_perso( dx, dy )
        
    def keyReleaseEvent ( self, event ) :
        None
        
    def mousePressEvent ( self, event ) :
        None
        
        
        
        
        
        
        
        
        
        
        
        