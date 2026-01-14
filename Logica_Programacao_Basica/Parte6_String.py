#==========Strings==========
def calculo(valor):
    return valor * 100

nome = 'Andressa'
sobrenome = 'Monteiro'
altura = 1.58687

print("Nome: " + nome + sobrenome + "Altura:" + str(altura))

#Formatacao com format
print("Format")
linha_2 = '{} {} tem {:.3f}'.format(nome, sobrenome, altura)
linha_3 = '{0} {1} tem {2:.3f}'.format(nome, sobrenome, altura)

print(linha_2)
print(linha_3)
print("\n")

#Formatacao com f-string
print("f-string")

linha_1 = f'{nome} {sobrenome} tem {altura:.3f}'
print(linha_1)

preco = 5
taxa = 2.5

texto = f"O preço é {preco} reais."
print(texto)

texto = f"O preço é {preco:.2f} reais."
print(texto)

texto = f"O preço é {59:.2f} reais."
print(texto)

texto = f"O preço é {59*16} reais."
print(texto)

texto = f"O preço é {preco+(preco*taxa)} reais."
print(texto)

texto = f"É muito {'caro' if preco>10 else 'barato'}."
print(texto)

filme = "Esqueceram de mim"
texto = f"Meu filme favorito é {filme.upper()}."
print(texto)

texto = f"Teste de funções com string: {calculo(98)}."
print(texto)


