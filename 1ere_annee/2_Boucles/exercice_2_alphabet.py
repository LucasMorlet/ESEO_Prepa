# Le décalage est la différence entre majuscule et minuscule
decalage = ord ('A') - ord ('a')

# Comme les lettres sont des nombres, on peut aller de 'a' à 'z'
for c in range ( ord('a'), ord('z') + 1 ) :
    print ( chr(c), end="" )
    # On ajoute le décalage pour transformer une minuscule en majuscule
    print ( chr ( c + decalage ), end="" )