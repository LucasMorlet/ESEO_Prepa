import sys 
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget   

# Les fenêtres
from PyQt5.QtWidgets import QMainWindow         # Fenêtre principale
from PyQt5.QtWidgets import QFrame              # Autres fenêtres
from PyQt5.QtWidgets import QDialog             # Les pop-up

# Les boutons
from PyQt5.QtWidgets import QButtonGroup        # Groupe de boutons
from PyQt5.QtWidgets import QPushButton         # Les boutons    
from PyQt5.QtWidgets import QRadioButton        # Les boutons radios
from PyQt5.QtWidgets import QCheckBox           # Les cases à cocher 

# Les listes
from PyQt5.QtWidgets import QComboBox           # Les listes déroulantes
from PyQt5.QtWidgets import QSpinBox            # Les Spin-box 
from PyQt5.QtWidgets import QDoubleSpinBox      # Les Spin-box décimales
from PyQt5.QtWidgets import QDial               # Les potentiomètres
from PyQt5.QtWidgets import QSlider             # Les sliders

# Le texte
from PyQt5.QtWidgets import QLineEdit           # Zone de texte d'une seule ligne
from PyQt5.QtWidgets import QTextEdit           # Zone de texte sur plusieurs lignes

# Les menus
from PyQt5.QtWidgets import QAction 
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar                 # Les menus
from PyQt5.QtWidgets import QTabBar
from PyQt5.QtWidgets import QTabWidget                   # Les onglets

# Les widgets d'organisation
from PyQt5.QtWidgets import QGroupBox           # 
from PyQt5.QtWidgets import QStackedWidget      # 
from PyQt5.QtWidgets import QTabWidget          # 

# Les affichages 
from PyQt5.QtWidgets import QLabel              # Les étiquettes
from PyQt5.QtWidgets import QProgressBar        # Barre de chargement
from PyQt5.QtWidgets import QLCDNumber          # Affichage LCD

# La gestions des dates
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QTimeEdit
from PyQt5.QtWidgets import QCalendarWidget # Les calendriers

class MainWindow ( QMainWindow ) :

    def __init__ ( self ) :
        QWidget.__init__ ( self )
        self.setWindowTitle ( "Exemples PyQt" )
        self.init_components()
        self.init_style()
        self.init_layout()
        self.show()
        
    def init_components ( self ) :
        self.setCentralWidget ( QGroupBox() )
        self.bouton1 = QPushButton ( "Bouton 1" )
        self.bouton2 = QPushButton ( "Bouton 2" )
        self.bouton3 = QPushButton ( "Bouton 3" )
        self.bouton4 = QPushButton ( "Bouton 4" )
        
        # text-align: left
        
    def init_style ( self ) :  
        self.bouton1.setStyleSheet ( "font : bold 'Times New Roman'" )
        self.bouton2.setStyleSheet ( "font : italic 'Times New Roman'" )
        self.bouton3.setStyleSheet ( "font : bold italic 'Times New Roman'" )
        self.bouton4.setStyleSheet ( "" )
        
    def init_layout ( self ) :
        self.layout = QVBoxLayout()
        self.centralWidget().setLayout ( self.layout )
        self.layout.addWidget ( self.bouton1 )
        self.layout.addWidget ( self.bouton2 )
        self.layout.addWidget ( self.bouton3 )
        self.layout.addWidget ( self.bouton4 )
        
# Application principale        
app = QApplication.instance()
if not app :
    app = QApplication ( sys.argv )

main_window = MainWindow()
app.exec()