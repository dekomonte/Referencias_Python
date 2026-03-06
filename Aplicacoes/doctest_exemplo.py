#Doctest - Exemplo de como usar
def operacao(x,y):

    """ Teste da funcao operacao
    >>> operacao(2,4)
    8

    >>> operacao(5,9)
    45

    >>> operacao(8,7)
    56
    """

    return x*y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
