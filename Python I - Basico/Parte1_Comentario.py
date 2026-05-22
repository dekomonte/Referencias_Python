#=====Docstrings=====
#String literal usada para documentar trechos de código como módulos, classes ou funções

"""
Docstrings
Nao eh um comentario;
O interpretador le;
"""

'''
Docstrings
Nao eh um comentario;
O interpretador le;   
'''

def test(x):
    '''
    Info: this function tests and prints param x
    '''
    print(x)

help(test)

print(test.__doc__)

#=====Comentarios=====
# Isso eh um comentario
# Python é uma linguagem interpretada
