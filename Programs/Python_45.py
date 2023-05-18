year = int(input("Digite o ano: "))

if year < 1582:
    print("Não está dentro do período do calendário gregoriano")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
