tab = [0]*10
print ( tab )

for i in range ( len(tab) ) :
    tab[i] = i+1
print ( tab )   
    
for i in range ( len(tab) ) :
    tab[i] = tab[i] * tab[i]
print ( tab )

print ( tab[12] )