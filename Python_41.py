# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número
# é o maior deles.
# Em breve verificaremos isso.
largest_number = number1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number2 > largest_number:
    largest_number = number2
 
# Nós verificamos se o terceiro número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number3 > largest_number:
    largest_number = number3
 
# Imprimir o resultado
print("O maior número é:", largest_number)
