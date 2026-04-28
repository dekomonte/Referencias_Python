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

