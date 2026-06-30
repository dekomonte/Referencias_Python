#Decorator Pattern
from time import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('**********')
        func(*args, **kwargs) #a função é chamada aqui
        print('**********')
    return wrapper

@my_decorator
def my_func(zero,frase1="olá meu nome é Rossil", frase2="Batman melhor que todos"):
    print(zero,frase1,frase2)

my_func('Na na na nana na')

#Example
def performance(funcao):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = funcao(*args, **kwargs)
        t2 = time()
        print(f"Tempo decorrido:{t2-t1} s")
        return result
    return wrapper

@performance
def f():
    for i in range(1000):
        print("BBzão")

f()
