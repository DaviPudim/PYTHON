hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
mins = mins + dura # encontre um total de todos os minutos
hour = hour + mins // 60 # encontre um número de horas escondido em minutos e atualize a hora
mins = mins % 60 # minutos corretos para cair no intervalo (0..59)
hour = hour % 24 # horas corretas para cair no intervalo (0..23)
print(hour, ":", mins, sep='')


