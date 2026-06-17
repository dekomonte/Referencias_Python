# ===== Comprehensions =====
#list, set, dictionary

# == List Comprehensions ==
print("List Comprehensions")
lista = []

for char in 'hello':
    lista.append(char)

print(lista)

#Existe um modo mais rápido de fazer isso?
#list comprehensions

#my_list = [param for param in iterable]
lista2 = [char for char in 'hello']
print(lista2)

lista3 = [numero for numero in range(10)]
print(lista3)

lista4 = [numero*2 for numero in range(10)]
print(lista4)

lista5 = [numero**2 for numero in range(10)]
print(lista5)

lista6 = [numero**2 for numero in range(10) if numero%2 == 0]
print(lista6)

# == Set and Dictionary Comprehensions ==

#Sets são simples, usa a mesma forma das listas só que entre {}
print("Sets Comprehensions")
conjunto = {char for char in 'hello'}
print(conjunto)

conjunto2 = {numero for numero in range(10)}
print(conjunto2)

conjunto3 = {numero**2 for numero in range(10)}
print(conjunto3)

conjunto4 = {numero**2 for numero in range(10) if numero%2 == 0}
print(conjunto4)

#Dictionary
#my_dict = {key:value}
print("Dictionary Comprehensions")

my_dict = {num:num*2 for num in [1,3,4]}
print(my_dict)
