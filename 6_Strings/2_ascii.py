decal = ord('A') - ord ('a')

for carac in range ( ord ('a'), ord('z')+1 ) :
    print ( chr(carac), end="" )
    print ( chr(carac + decal), end="" )