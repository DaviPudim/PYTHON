    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você nnão tem inseriu qualquer número.")

