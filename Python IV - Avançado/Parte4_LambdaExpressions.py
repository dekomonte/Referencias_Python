# ===== Functional Programming =====

# == Lambda Expressions ==
#Small anonymous function
#Function that you don't need to run more than one time
#Can take any number of arguments, but can only have one expression
#lambda param: action(param)

from functools import reduce

#Example
lista = [2,7,15]
print(list(map(lambda x: x**2, lista)))
print(list(map(lambda x: x*2, lista)))

#Example
y = lambda x: x+4
print(y(6))

#Example
z = lambda x,a,b,c: x**3 + a + b + c
print(z(5,3,2,1))

#Example
def funcao(n):
    return lambda i: i*n

print(funcao(5)(10))
print(funcao(2)(9))

#Example
numeros = [51,5,2,7,3,2385]
impares = list(filter(lambda x: x%2 != 0, numeros))
print(impares)

#Example
soma = lambda x, y: x + y
print(soma(7,9))

soma2 = (lambda x, y: x + y)(7,9)
print(soma2)

#Example
lista2 = [1,5,3,4,5,6,1,8,34,12,8,7,9,0,1,45]
print(reduce(lambda x, y: x+y, lista2))

soma3=0
for n in lista2:
    soma3=soma3+n
print(soma3)

#Example
usuarios = [
    {"nome": "Pedro","idade": 37 },
    {"nome": "Thiago","idade": 12},
    {"nome": "Joao","idade": 3 },
    {"nome": "Barquinho","idade": 78},
    {"nome": "Paulo","idade": 45 },
    {"nome": "Gabriel","idade": 8}
]

ordenar_idade = sorted(usuarios, key=lambda x: x["idade"])
print(ordenar_idade)

ordenar_nome = sorted(usuarios, key=lambda x: x["nome"])
print(ordenar_nome)

ordenar_usuarios = sorted(usuarios, key=lambda x: (-x["idade"],x["nome"]))
print(ordenar_usuarios)

mais_velho = max(usuarios, key=lambda x: x["idade"])
print(mais_velho)

mais_novo = min(usuarios, key=lambda x: x["idade"])
print(mais_novo)

#Example
numeros2 = [2,1,4,5,6,754,76,789,4,3,7,9,0,1]
pares_quadrado = list(map(lambda x: x**2, filter(lambda x: x%2==0, numeros2)))
print(pares_quadrado)

pares_quadrado2 = [x**2 for x in numeros2 if x % 2 == 0]
print(pares_quadrado2)
