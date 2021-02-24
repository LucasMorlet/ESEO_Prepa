# On ne considère que des minuscules
def caractere_plus_3 ( car ) :
    # On convertit le caractère en nombre
    n = ord(car)
    # On se passe entre 0 et 25
    n = n - ord('a')
    # On ajoute 3
    n = n + 3
    # On fait un modulo au cas où on soit "plus loin que z"
    n = n % 26
    # On modifie la lettre
    n = n + ord('a')
    # On renvoie le caractère
    return chr ( n )
    
def caractere_moins_3 ( car ) :
    n = ord(car)
    n = n - ord('a')
    n = n + 23 # +23 est équivalent à -3
    n = n % 26
    n = n + ord('a')
    return chr ( n )
    
def cesar ( string ) :
    string = string.lower()
    res = ""
    for i in range ( len ( string ) ) :
        lettre_courante = string[i]
        nouvelle_lettre = caractere_plus_3 ( lettre_courante )
        res = res + nouvelle_lettre
        
    return res.upper()
    
def inv_cesar ( string ) :
    string = string.lower()
    res = ""
    for i in range ( len ( string ) ) :
        lettre_courante = string[i]
        nouvelle_lettre = caractere_moins_3 ( lettre_courante )
        res = res + nouvelle_lettre
        
    return res.upper()
  
# Test basique
mot = "CESAR"       
print ( mot, end = " -> " )
mot = cesar(mot)
print ( mot, end = " -> " )
mot = inv_cesar(mot)
print ( mot )

# Test avec rebouclage
mot = "VWXYZ"       
print ( mot, end = " -> " )
mot = cesar(mot)
print ( mot, end = " -> " )
mot = inv_cesar(mot)
print ( mot )