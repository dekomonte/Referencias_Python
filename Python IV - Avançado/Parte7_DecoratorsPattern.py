#Decorator Pattern
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
