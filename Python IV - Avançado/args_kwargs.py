#=====Python *args and **kwargs=====
#Sometimes you may not know how many arguments that will be passed into your function
#*args and **kwargs allow functions to accept a unknown number of arguments

#Example - *args
def nomes(*args):
    print(args)
    print("Tipo: ", type(args))
    print("Tamanho: ", len(args))
    for item in args:
        print(item)

nomes("Goku", "Gohan", "Tolstoi", "Machado")
nomes("Eduardo","Mônica","Goku", "Gohan", "Tolstoi", "Machado")
nomes("The Boys",8.5,"Goku", True, "Tolstoi", 1)
print("*args gera uma tupla")

#You can combine regular parameters with *args
#Regular parameters must come before *args

#Example - **kwargs
#**kwargs - you don't know how many keywords arguments will be passed
#**kwargs parameter allows a function to accept any number of keyword arguments
def nomes_e_outras(**kwargs):
    print(kwargs)
    print("Tipo: ", type(kwargs))
    print("Tamanho: ", len(kwargs))

nomes_e_outras(nome = "Luke",sobrenome = "Skywalker",idade = 18 ,sabedoria = 9.8, arma ="Sabre de Luz")
print("**kwargs gera um dicionário")

#Example
def exemplo_completo(titulo, *args, **kwargs):
    print("=====Exemplo de completo=====")
    print("Título: ", titulo)
    print("args: ", args, type(args))
    print("kwargs: ", kwargs, type(kwargs))
    print("*args gera uma tupla")
    print("**kwargs gera um dicionário")

exemplo_completo("*args e **kwargs", "Leia", "Goku", "Tolstoi", nome = "Han Solo", idade = 65)

#Casos práticos: loggers, decorators, criação dinâmica de objeto, combinação de dicionários
