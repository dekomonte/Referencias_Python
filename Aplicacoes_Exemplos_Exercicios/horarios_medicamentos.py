# Horários para tomar remédio - script mais tosco e menos robusto possível

# ["nome do remedio", primeiro horario, intervalo]
remedios = [
    ["Ibuprofeno", 8, 8],
    ["Dipirona", 8, 6],
    ["Ondansetrona", 8, 4]
]

for remedio in remedios:
    print(remedio[0])
    hora = remedio[1]
    intervalo = remedio[2]
    while hora <= 24:
        print(hora)
        hora = hora+intervalo
