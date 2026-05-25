# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list

def maior_par(numeros):
    maior_par = 0
    for x in numeros:
        if x%2 == 0 and x>maior_par:
            maior_par = x
    return maior_par

lista_numero = [342,5,76,8,1,3,54,89,354,3,54,23,7,734,2,7,1006]

resposta = maior_par(lista_numero)

print("O maior par da lista: ", resposta)
