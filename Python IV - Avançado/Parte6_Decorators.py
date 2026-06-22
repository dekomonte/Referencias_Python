# ===== Decorators =====
#Decorators let you add extra behavior to a function, without changing the function's code
#A decorator is a function that takes another function as input and returns a new function

#Example
#Decorators funcionam por causa dessa funcionalidade do Python
def minha_funcao(funcao):
    funcao()

def teste():
    print("Oi, eu sou o Goku!")

a = minha_funcao(teste)

#Higher Order Function
#It's a function that returns another function
#Any function that either accepts a function as a parameter
def exemplo():
    def exemplo2():
        return 2
    return exemplo2

b = exemplo()
print(b)

#Decorator
#uma função que recebe outra função como argumento,
#adiciona alguma lógica a ela e retorna uma nova função modificada
def my_decorator(funcao):
    def wrap_funcao():
        print("======")
        funcao()
        print("======")
    return wrap_funcao

@my_decorator
def hello():
    print("Oi, eu sou o Goku 2!")

@my_decorator
def tchau():
    print("tchau tchau")

hello()
tchau()

print("É o mesmo que fazer isso:") #Mais confuso
my_decorator(hello)()
my_decorator(tchau)()
