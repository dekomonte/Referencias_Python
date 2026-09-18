# ========= Generators ==========

# Allows us to generate a sequence of values over time
# range is a generator
# Functions that can pause and resume their execution
# Não carrega todos os elementos na memória de uma so vez

def fibonacci():
  a, b = 0, 1
  while True:
    yield a # -> Pausa a execução, envia o valor atual de volta para quem chamou e salva o estado de todas as variáveis
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci() # Cria o objeto gerador (não executa o código ainda)

print(gen)
print(next(gen)) # Executa até encontrar o próximo 'yield'
print(next(gen))
print(next(gen))
print(next(gen))
