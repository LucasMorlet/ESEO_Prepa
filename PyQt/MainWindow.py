from GraphicsScene import *
from random import random
import time
import sys
from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QObject)
from PyQt5.QtGui import (QBrush, QColor, QPainter,QPen,QFont)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                                QGraphicsLineItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QLabel, QLineEdit, QPushButton,QWidget, QMainWindow)

class MainWindow ( QMainWindow ) :

    def __init__ ( self, scene ) :
        QWidget.__init__ ( self )
        self.setWindowTitle ( "Exemples QGraphics" )
        self.init_components()
        self.scene = scene
        self.init_scene( self.scene )
        self.init_layout()
        self.show()
        
    def init_scene ( self, scene ) :
        self.gscene = GraphicsScene( scene )
        self.vue = QGraphicsView ( self.gscene )    
        
    def init_components ( self ) :
        self.setCentralWidget ( QGroupBox() )
        
    def init_layout ( self ) :
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.vue )
        self.resize ( 800, 600 )
        