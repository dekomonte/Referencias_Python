#==========#Data Structure==========

#Tuple
#Immutables Lists
#Faster then Lists

#Exemplo 1
minha_tupla = (1,2,3,4,5,6) 

print(minha_tupla)
print(3 in minha_tupla)

exemplo = {
    (1,2): ['a','b','c'],
    'nome': 'Fulano da Silva',
    'idade': 2
}

print(exemplo)
print(type(exemplo))
print(exemplo[(1,2)])

#Exemplo 2
minha_tupla = (1,2,3,4,5,6) 
minha_tupla2 = minha_tupla[1:4]
print(minha_tupla2)

x,y,z, *other = (1,2,3,4,5,6)
print(x)
print(y)
print(z)
print(other)

#Exemplo 3 - Methods
minha_tupla = (1,2,3,4,5,5,6)

print('len: ', len(minha_tupla))
print('index: ',minha_tupla.index(3))
print('count: ',minha_tupla.count(5))
