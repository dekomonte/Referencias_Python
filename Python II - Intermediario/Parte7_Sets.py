#==========#Data Structure==========

#Set
#Unordered collections of unique objects

#Exemplo 1
my_set = {1,2,3,4,5,6}
print(my_set)

my_set = {1,2,3,4,4,4,5,6} #Tudo é único
print(my_set)

my_set.add(4)
my_set.add(5)
my_set.add(100)
print(my_set)

minha_lista = [1,2,3,4,4,4,5,6]
print(set(minha_lista))

#Exemplo 2
my_set2 = {"laranja","maçã","arroz","Flamengo", 1, 44, False}
print(my_set2)
print("len: ",len(my_set2))

#Exemplo 3
conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8,9,10,11,12,13,14,15}

print("difference(): ",conjunto1.difference(conjunto2))

conjunto2.discard(7)
print("discard(): ", conjunto2)

print("intersection(): ",conjunto1.intersection(conjunto2))
