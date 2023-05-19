x = 10
 
if x > 5: # True
    if x == 6: # False
        print("aninhado: x == 6")
    elif x == 10: # True
        print("aninhado: x == 10")
    else:
        print("aninhado: else")
else:
    print("else")
