string = "Hello World !"

print ( "La chaine a une longueur de :", len ( string ) )
print ( "Il y a", string.count('o'), "'o'" )
print ( "Le premier 'o' est en position :", string.find('o') )
print ( "Il y a", string.count(' ')+1, " mots" )
print ( string.upper() )
print ( string.lower() )
print ( string.replace ( "o", "a" ) )



# Affichage à l'envers
tab = string.split(' ')
print ( tab )
res = ""
for i in reversed ( range ( len ( tab ) ) ) :
    res = res + tab [ i ] + " "
print ( res )