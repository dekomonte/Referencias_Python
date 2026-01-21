#==========#Data Structure==========

#Lists Methods
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

#adding
lista.append(100) #	Adds an element at the end of the list
print(lista)

lista.insert(3,'aqui') # Adds an element at the specified position
print(lista)

lista2 = ['arroz','feijao']
lista.extend(lista2) # Add the elements of a list to the end of the current list
print(lista)

#removing
lista.pop() # Removes the element at the specified position - default: the last item on the list
print(lista)

lista.pop(0) # Removes the element at the specified position
print(lista)

lista.remove(3) # Removes the FIRST item with the specified value
print(lista)

lista.clear() # Removes all the elements from the list
print(lista)

#Lists Methods 2
lista = [1,2,3,4,5,6,7,8,9,10]
print("Parte 2: ", lista)

lista3 = ['a', 'r', 'j', 'v', 'e', 't']

#index
print(lista.index(3)) # Qual o index do elemento 

print(lista3)
print(lista3.index('t')) # Returns the index of the first element with the specified value

print('c' in lista3) # Check if a value is present in a sequence
print('e' in lista3)

print(lista.count(4)) # Returns the number of elements with the specified value

#Lists Methods 3
print(lista3)

lista3.sort() # Ordena
print(lista3)

# methods != functions
lista3 = ['a', 'r', 'j', 'v', 'e', 't']
print(sorted(lista3)) # Produz uma copia da lista e ordena

lista4 = lista2.copy() # Faz a copia de uma lista
print(lista4)

lista3.reverse() # Inverte os elementos da lista
print(lista3)


lista3 = ['a', 'r', 'j', 'v', 'e', 't']
lista3.sort()
lista3.reverse()
print(lista3)
