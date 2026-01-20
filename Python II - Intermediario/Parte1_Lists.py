#==========#Data Structure==========

#Lists are like arrays
li = [1,2,3,4]
li2 = ['a','b']
li3 = [1, 'a', True]

print(li)
print(li2)
print(li3)

#List Slicing
carrinho_compras = ['notebooks', 'brinquedos', 'frutas', 'verduras','xampu', 'panela']
print(carrinho_compras[0:2])
carrinho_compras[1] = 'carne'
print(carrinho_compras[0::2])

print("Caso 1:")
frutas = ['banana','uva','kiwi', 'melão', 'maçã', 'abacaxi']
novo_frutas = frutas #Atribui
novo_frutas[2] = 'limão' #fruta também é modificada
print(frutas)
print(novo_frutas)

print("Caso 2:")
frutas = ['banana','uva','kiwi', 'melão', 'maçã', 'abacaxi']
novo_frutas = frutas[:] #Copia toda lista
novo_frutas[2] = 'limão' #fruta não é modificada
print(frutas)
print(novo_frutas)
