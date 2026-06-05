#==========frozenset()==========

# Function returns an unchangeable frozenset object
# it looks like sets, but immutable
# Hashable version of a set

print("Exemplo")
lista = ['x','y',1,2,3,4,5,6]
print("Lista original: ", lista)
print(type(lista))

imutavel = frozenset(lista)
print("Frozenset: ", imutavel)
print(type(imutavel))

#=====Operações=====
x = frozenset([1,2,3,4,5,6])
y = frozenset([0,1,11,21,31,41,51,61])

print(x)
print(y)

#Checar se um item pertence ao conjunto
if 3 in x:
    print("3 in x")
else:
    print("3 is not in x")

#Operações de conjunto
print("x | y", x | y)
print("x & y", x & y)
print("x - y", x - y)
