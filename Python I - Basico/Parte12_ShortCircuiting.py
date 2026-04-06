#==========Short Circuiting==========
# Interpretador interrompe a execução de uma operação booleana assim que o resultado final pode ser determinado
# and e or 

# Exemplo
divisor = 0

if divisor != 0 and (10/divisor) < 1: # O interpretador não chega na segunda condição pois a primeira já é FALSA
    print("Uhuul")
else:
    print("Operação não pode ser executada")

