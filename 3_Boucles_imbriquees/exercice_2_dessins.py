# L
for i in range ( 5 ) :
    for j in range ( 5 ) :
        if j == 0 or i == 4 :
            print ( "X", end="" )
        else :
            print ( " ", end="" )
    print ( "" )
print ( "" )

# C
for i in range ( 5 ) :
    for j in range ( 5 ) :
        if j == 0 or i == 0 or i == 4 :
            print ( "X", end="" )
        else :
            print ( " ", end="" )
    print ( "" )
print ( "" )

# U
for i in range ( 5 ) :
    for j in range ( 5 ) :
        if j == 0 or i == 4 or j == 4 :
            print ( "X", end="" )
        else :
            print ( " ", end="" )
    print ( "" )
print ( "" )

# O
for i in range ( 5 ) :
    for j in range ( 5 ) :
        if j == 0 or j == 4 or i == 0 or i == 4 :
            print ( "X", end="" )
        else :
            print ( " ", end="" )
    print ( "" )
print ( "" )

# N
for i in range ( 5 ) :
    for j in range ( 5 ) :
        if j == 0 or j == 4 or i == j :
            print ( "X", end="" )
        else :
            print ( " ", end="" )
    print ( "" )
print ( "" )

# Z
for i in range ( 5 ) :
    for j in range ( 5 ) :
        if i == 0 or i == 4 or j == 4-i :
            print ( "X", end="" )
        else :
            print ( " ", end="" )
    print ( "" )
print ( "" )