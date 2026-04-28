#Exercise: Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

print("===== Árvore =====")
for x in picture:
    for y in x:
        if y == 0: print(" ", end="")
        # if y == 1: print("*", end="")
        else: print("*", end="") #Assumindo que picture será sempre 0 ou 1
    print(" ")
print("\n")

# EXTRA - Inverter a imagem (sugestão do Lucas)
print("===== Árvore Invertida =====")
tamanho = len(picture)
# print(tamanho)
for i in range(tamanho-1,-1,-1):
    for item in picture[i]:
        if item == 0: print(" ", end="")
        # if y == 1: print("*", end="")
        else: print("*", end="") #Assumindo que picture será sempre 0 ou 1
    print(" ")

print("===== Árvore Invertida (Lucas) =====")
for x in picture[::-1]:
    for y in x:
        if y == 0: print(" ", end="")
        # if y == 1: print("*", end="")
        else: print("*", end="") #Assumindo que picture será sempre 0 ou 1
    print(" ")
