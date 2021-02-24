# Conversion caractère vers numéro
caractere = 'N'
print ( "Le numéro de", caractere, "est :", ord(caractere) )

# Conversion numéro vers caractère
numero = 93
print ( "Le caractère numéro", numero, "est :", chr(numero) )

# Utilisation des caractères comme nombre pour le calcul
lettre = 'A'
decalage = 4
res = chr ( ord(lettre) + decalage )
print ( lettre, "+", decalage, "=", res )

# Conversion chaine de caractère vers nombre entier
nombre_en_caractere = "6"
nombre_en_entier = 2
somme = int(nombre_en_caractere) + nombre_en_entier
print ( nombre_en_caractere, "+", nombre_en_entier, "=", somme )

# Conversion chaine de caractère vers nombre décimal
decimal_en_caractere = "18.2"
nombre_en_decimal = 4.6
somme_decimale = float(decimal_en_caractere) + nombre_en_decimal
print ( decimal_en_caractere, "+", nombre_en_decimal, "=", somme_decimale )