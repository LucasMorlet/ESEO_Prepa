import os
import sys

path_actuel = os.path.dirname( __file__ )
path_classe = os.path.join( path_actuel, "core" )
sys.path.append( path_classe )

from Partie import *

p = Partie ( 5, 5, 5 )
p.joue()