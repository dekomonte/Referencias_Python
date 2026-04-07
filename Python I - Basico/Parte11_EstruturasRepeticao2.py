#==========Estruturas de Repeticao==========
#FOR -> 

print("Lista")
for item in [1,2,3,4,5]:
    print(item)

print("Tupla")
for item in (1,2,3,4,5):
    print(item)

for item in [1,2,3,4,5]:
    for x in ['a','b','c']:
        print(item,x)

print("String")
for item in "Estou estudando Python!":
    print(item)

# iterable - list, dictionary, tuple, set, string
# iterate -> oe by one check each item in the collection

print("Dicionário")

usuario = {
    'nome': 'Andressa',
    'idade': '28',
    'pode_nadar': True,
    'atividade_favorita': "jogar"
}

for item in usuario.items():
    key, value = item
    print(key, value)

for key, value in usuario.items():
    print(key, value)

for item in usuario.items():
    print(item)

for item in usuario.keys():
    print(item)

for item in usuario.values():
    print(item)
