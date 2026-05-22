# Function are useful when you have things that you want to do over and over
def minha_funcao_de_dizer_oi():
    print("Oi")

def minha_funcao_de_dizer_qualquer_coisa(palavra):
    print(f"Qualquer coisa:{palavra}")

def minha_funcao_para_mostrar_retorno(x,y):
    return x+y

minha_funcao_de_dizer_oi()

for i in range(10):
    minha_funcao_de_dizer_oi()

minha_funcao_de_dizer_qualquer_coisa('Qualquer coisa')
minha_funcao_de_dizer_qualquer_coisa('Brincando de parâmetros')
minha_funcao_de_dizer_qualquer_coisa(8)
minha_funcao_de_dizer_qualquer_coisa(1123.2342)

#positional arguments -> the position matters
#keyword arguments
#default parameters

print(minha_funcao_para_mostrar_retorno(3,9))
print(minha_funcao_para_mostrar_retorno(33,29))
