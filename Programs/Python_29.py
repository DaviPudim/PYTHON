leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
hypo = round(hypo,2)
print("O comprimento da hipotenusa é", hypo)

