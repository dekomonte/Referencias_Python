#==========#Data Structure==========

#Dictionary Methods
usuario = {
    'nome': 'Saymon',
    'sobrenome': 'Carvalho',
    'skills': [1,7,98,2323],
    'idade': 89,
    'dia':2,
    'cpf': '098098098098'
}

#get() - returns the value of the item with the specified key
print(usuario.get('age'))
print(usuario.get('age',34)) #Default


#Outra forma de criar um dicionário (menos usada)
usuario2 = dict(nome='Cláudio', idade = 68, skills = [43,6,0,90])
print(usuario)
print(usuario2)

#Verifica se a chave existe no dicionário
print('age' in usuario)
print('nome' in usuario)

print('Saymon' in usuario.values())

#Deixa o dicionário vazio
usuario2.clear()
print(usuario2)

#Faz uma cópia do dicionário
usuario3 = usuario.copy()
print("Original: ",usuario)
print("Cópia: ",usuario3)

#Remove um item do dicionário
usuario.pop('nome')
print(usuario)

#Remove o último item do dicionário
usuario.popitem()
print(usuario)

#Ataliza um item
usuario.update({'idade': 55})
print(usuario)

#Returns a list of all the values in the dictionary
print(usuario.values())
