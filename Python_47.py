secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

while True:
    user_number = int(input("Tente adivinhar o número secreto: "))

    if user_number == secret_number:
        print("Muito bem, trouxa! Você está livre agora.")
        break  # Sai do loop while quando o número é adivinhado corretamente
    else:
        print("Ha ha! Você está preso no meu loop!")
