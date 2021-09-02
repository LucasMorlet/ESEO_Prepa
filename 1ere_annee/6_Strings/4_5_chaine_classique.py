def affichage_caractere ( string ) :
    for i in range ( len ( string ) ) :
        print ( string[i] )

def compte_lettre ( string, car ) :
    nb = 0
    for i in range ( len ( string ) ) :
        if ( string[i] == car ) :
            nb = nb + 1
    return nb

def premiere_lettre ( string, car ) :
    nb = 0
    for i in range ( len ( string ) ) :
        if ( string[i] == car ) :
            return i
    return -1 # Pas trouvé

def compte_mots ( string ) :
    return 1 + compte_lettre ( string, ' ' )
    
def remplace ( string, old, new ) :
    res = ""
    for i in range ( len ( string ) ) :
        if ( string[i] == old ) :
            res = res + new
        else :
            res = res + string[i]
    return res
    
def majuscule ( string ) :
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    minuscule_vers_majuscule = A - a
    
    res = ""
    for i in range ( len ( string ) ) :
        num = ord ( string[i] )
        if ( a <= num and num <= z ) :
            res = res + chr ( num + minuscule_vers_majuscule )
        else :
            res = res + string[i]
    return res
    
def minuscule ( string ) :
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    majuscule_vers_minuscule = a - A
    
    res = ""
    for i in range ( len ( string ) ) :
        num = ord ( string[i] )
        if ( A <= num and num <= Z ) :
            res = res + chr ( num + majuscule_vers_minuscule )
        else :
            res = res + string[i]
    return res

string = "Hello World !"
affichage_caractere ( string )
print ( "Il y a", compte_lettre(string, 'o'), "'o'" )
print ( "Le premier 'o' est en position :", premiere_lettre(string, 'o') )
print ( "Il y a", compte_mots(string), " mots" )
print ( remplace ( string, 'o', 'a' ) )
print ( majuscule(string) )
print ( minuscule(string) )