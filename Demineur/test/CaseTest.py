import os
import sys

path_actuel = os.path.dirname( __file__ )
path_parent = os.path.dirname( path_actuel )
path_classe = os.path.join( path_parent, "core" )
sys.path.append( path_classe )

from Case import *

print()          
print ( "*** Test de la classe Case ***" )
c = Case()

print()
print ( "Case cachee              :", end = " ")
c.afficheConsole()

c.switchDrapeau()
print()
print ( "Case drapeau             :", end = " ")
c.afficheConsole()

c.switchDrapeau()
print()
print ( "Case cachee a nouveau    :", end = " ")
c.afficheConsole()

c.revele()
print()
print ( "Case vide                :", end = " ")
c.afficheConsole()

c.setValeur(7)
print()
print ( "Case contenant un nombre :", end = " ")
c.afficheConsole()

c.devientBombe()
print()
print ( "Case contenant une bombe :", end = " ")
c.afficheConsole()

print()
print()
print ( "*** Fin du test de la classe Case ***" )
print()