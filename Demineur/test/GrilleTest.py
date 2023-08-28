import os
import sys

path_actuel = os.path.dirname( __file__ )
path_parent = os.path.dirname( path_actuel )
path_classe = os.path.join( path_parent, "core" )
sys.path.append( path_classe )

from Grille import *

print()          
print ( "*** Test de la classe Grille ***" )
g = Grille( 5, 5, 5 )

print()
g.afficheConsole()

print()
g.reveleTotalite()
g.afficheConsole()

print()
g = Grille( 5, 5, 5 )
g.reveleCase ( 2, 0 )
g.afficheConsole()

print()
g.reveleAlentours( 3, 4 )
g.afficheConsole()

print()
g.reveleCase ( 2, 0 )
g.switchDrapeau ( 4, 0 )
g.reveleCase ( 4, 0 )
print () 
g.afficheConsole()

print()
print ( "*** Fin du test de la classe Grille ***" )
print()