#OOP - Múltipla Herança

#Uma classe filha herda atributos e métodos de duas ou mais classes mães

#Example
class Moto:

    def andar(self):
        return "Pilotando minha motinha"

class Caminhao:

    def caminhao(self):
        return "Muita areia pro seu caminhãozinho"

class MotoCaminhao(Moto,Caminhao):
    print("MotoCaminhao")

hibrido = MotoCaminhao()
print(hibrido.andar())
print(hibrido.caminhao())

#==========O Problema do Diamante==========
#Problema: duas classes mães com métodos com mesmo nome
#Solução: MRO (Method Resolution Order)
#   1. A ordem em que você declara as classes mães importa
#   2. Python sempre vai procurar o método na classe mais específica (filha)
#   antes de subir para as classes mais genéricas (mães)

#Example
class A:
    def grito(self):
        return "Fala da classe A"

class B(A):
    def grito(self):
        return "Fala da classe B"

class C(A):
    def grito(self):
        return "Fala da classe C"

class D(B, C):
    print("Classe D")

instancia = D()
print(instancia.grito())
print(D.__mro__)

#Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes
