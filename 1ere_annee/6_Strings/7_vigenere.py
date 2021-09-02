def estUneMajuscule ( nombre ) :
    if ord('A') <= nombre and nombre <= ord('Z') :
        return True
    return False
    
def estUneMinuscule ( nombre ) :
    if ord('a') <= nombre and nombre <= ord('z') :
        return True
    return False

def lettre_vers_nombre ( car ) :
    nombre = ord ( car )
    
    # Si c'est une minuscule
    if estUneMinuscule ( nombre ) :
        return nombre - ord ('a')
        
    # Si c'est une majuscule
    if estUneMajuscule( nombre ) :
        return nombre - ord ('A')
        
    # Si c'est un autre caractère
    return 0
    
    

def decalage_caractere ( car, decal ) :

    nombre = ord( car )
    
    # Si le caractère n'est pas une lettre, je le renvoie tel quel
    if  not ( estUneMinuscule ( nombre ) ) and not ( estUneMajuscule ( nombre ) ) :
        return car
        
    nombre = ord( car )
    res = nombre + decal 
    
    # Si j'ai dépassé 'z'
    if nombre <= ord('z') and ord('z') < res :
        res = res - 26
     
    # Si j'ai dépassé 'Z'
    if nombre <= ord('Z') and ord('Z') < res :
        res = res - 26
        
    return chr(res)

def deroule_cle ( cle, taille ) :
    res = "";
    taille_cle = len ( cle )
    
    for i in range ( taille ) :
        res += cle[ i % taille_cle ]
        
    return res
    
def supprime_espace ( texte ) :
    res = ""
    for i in range ( len ( texte ) ) :
        if texte[i] != ' ' :
            res += texte[i]
    return res


def vigenere ( texte, cle ) :
    cle = deroule_cle ( cle, len ( texte ) )
    res = ""
    for i in range ( len ( texte ) ) :
        res += decalage_caractere ( texte[i], lettre_vers_nombre( cle[i] ) )
        
    return res
    
def inv_vigenere ( texte, cle ) :
    cle = deroule_cle ( cle, len ( texte ) )
    res = ""
    for i in range ( len ( texte ) ) :
        res += decalage_caractere ( texte[i], 26 - lettre_vers_nombre( cle[i] ) )
        
    return res
    
    
texte = "LeChiffreDeVigenere"
cle = "Amie"
chiffre = vigenere ( texte, cle )
dechiffre = inv_vigenere ( chiffre, cle )

print ( "***** Exemple 1 : uniquement des lettres *****" )
print()
print ( texte )
print ( deroule_cle ( cle, len ( texte ) ) )
print ( chiffre )
print ( dechiffre )

print ()
print ()
print ( "***** Exemple 2 : on rajoute des caractères spéciaux *****" )
print()

texte = "Une phrase assez longue (mais pas trop) pour tester les caracteres speciaux..."
cle = "Zw-Xn!kl@"
chiffre = vigenere ( texte, cle )
dechiffre = inv_vigenere ( chiffre, cle )

print ( texte )
print ( deroule_cle ( cle, len ( texte ) ) )
print ( chiffre )
print ( dechiffre )

print ()
print ()
print ( "***** Exemple 3 : on supprime les espaces *****" )
print()

texte = "Une phrase assez longue (mais pas trop) ou l'on supprime les espaces..."
texte_reduit = supprime_espace ( texte )
cle = "fs6Mk'9pM%"
chiffre = vigenere ( texte_reduit, cle )
dechiffre = inv_vigenere ( chiffre, cle )

print ( texte )
print ( texte_reduit )
print ( deroule_cle ( cle, len ( texte_reduit ) ) )
print ( chiffre )
print ( dechiffre )

    
