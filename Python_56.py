number = int(input("Digite um número natural: "))

count = 0
while number != 1:
    print(number)
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    count += 1

print(number)
print("Número de etapas:", count)


