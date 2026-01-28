#==========#Data Structure==========

#Dictionary
#It might be called a hash table, maybe map or objects in anothers languages
#Is a unordered key value pair

dictionary = {
    'a': 1, #key-value
    'b': 2
}

print(dictionary['b'])

#Exemplo 1
dicionario1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


print(dicionario1["brand"])
print(dicionario1['year'])
print(dicionario1['electric'])
print(dicionario1['colors'])

#Exemplo 2
lista = [
    {
        'a': [1,2,3],
        'b': [4,5,6],
        'x': True
    },
    {
        'a': [1,2,3],
        'b': 'oioioi',
        'x': False,
        'teste': 'teste'
    }
]

print(lista[0]['a'])
print(lista[0]['b'])
print(lista[0]['x'])

print(lista[1]['a'])
print(lista[1]['b'])
print(lista[1]['x'])
print(lista[1]['teste'])

#The key cannot change, it's immutable
#Exemplo 3 
dicionario3 = {
    '123': ['a','b','c'],
    '123': 'Bora Tubarões'
}

print(dicionario3['123']) #O primeiro registro é perdido
