from random import *

def genere_calendrier () :
    calendrier = [0]*6
    for i in range ( len ( calendrier ) ) :
        calendrier[i] = [0]*4
     
    ligne_courante = 0
    case_courante = 0 
    for i in range ( 1, 25 ) :
        calendrier[ligne_courante][case_courante] = i
        case_courante += 1
        if ( case_courante >= 4 ) :
            case_courante = 0
            ligne_courante += 1
         
    return calendrier
    
def melange_calendrier ( calendrier ) :
    for n in range ( 50 ) :
        i1 = int ( random() * len ( calendrier ) )
        j1 = int ( random() * len ( calendrier[0] ) )
        i2 = int ( random() * len ( calendrier ) )
        j2 = int ( random() * len ( calendrier[0] ) )
        
        tmp = calendrier[i1][j1]
        calendrier[i1][j1] = calendrier[i2][j2]
        calendrier[i2][j2] = tmp
    
    return calendrier
    
    
    
def affiche_calendrier ( calendrier ) :     
    for i in range ( len ( calendrier ) ) :
        print( calendrier[i] )


c = genere_calendrier()
c = melange_calendrier ( c )
affiche_calendrier ( c )