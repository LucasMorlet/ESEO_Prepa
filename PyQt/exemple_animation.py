from MainWindow import *
from Scene import *
import threading

app = QApplication.instance()
if not app :
    app = QApplication ( sys.argv )

scene = Scene()
main_window = MainWindow( scene )
    
app.exec()