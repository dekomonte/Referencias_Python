# ===== Functional Programming =====

# -> Pure Functions

# Given the same input, it will always return the same output
# A function should not produce any side effects
# (não modifica variáveis globais, não altera o banco de dados, não muda o DOM da página)

# Exemplo
def multiplica_por2(lista):
    nova_lista = []
    for item in lista:
        nova_lista.append(item * 2)
    return nova_lista

print(multiplica_por2([1, 2, 3, 4]))
print(multiplica_por2([2, 4, 5]))
print(multiplica_por2([19, 32, 78]))
