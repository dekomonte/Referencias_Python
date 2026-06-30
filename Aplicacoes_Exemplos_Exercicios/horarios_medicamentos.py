# Horários para tomar remédio - script mais tosco e menos robusto possível

# ["nome do remedio", primeiro horario, intervalo]
remedios = [
    ["Ibuprofeno", 10, 8],
    ["Dipirona", 9, 6]
    # ["Ondansetrona", 8, 8]
]

for remedio in remedios:
    print(remedio[0])
    hora = remedio[1]
    intervalo = remedio[2]
    while hora < 24:
        print(f"{hora}:00")
        hora = hora+intervalo
    if hora == 24:
        print(f"00:00")
    print("\n")
