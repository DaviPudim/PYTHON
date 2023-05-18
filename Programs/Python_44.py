income = float(input("Entre com os rendimentos: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.2 + (income - 85528) * 0.32

tax = round(tax, 0)

print("A taxa é:", tax, "thalers")
