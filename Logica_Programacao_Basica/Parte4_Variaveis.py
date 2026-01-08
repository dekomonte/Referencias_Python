#==========Variaveis==========
#PEP 8 – Style Guide for Python Code
#https://peps.python.org/pep-0008/

# Local da memória que grava uma informação que eu posso reutilizar sempre
# Mutável

nome = 'Andressa'
sobrenome = 'Monteiro'
apelido = 'dekomonte'
idade = 28


print("USUÁRIO CADASTRADO")
print("==========#=========#========")
print(nome + ' ' + sobrenome)
print(apelido)
print(idade)

cpf = '159753123x5'
rg = '999x999'

print('CPF: '+ cpf)
print('RG: ' + rg)

# DICA
a,b,c = 1,2,3
print("a,b,c: ",a,b,c)
print("a: ",a)
print("b: ",b)
print("c: ",c)


#==========Constantes==========
#Nao tem esse conceito em python
#Mas existe a convencao de usar letras maiusculas

PI = 3
RAIO = 2.5

print(PI)
print(RAIO)
