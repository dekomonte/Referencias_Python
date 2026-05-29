#OOP

#Classe -> Molde
#Objeto -> Instância da classe

#4 pillars of oop: Encapsulation, Abstraction, Inheritance, Polymorphism

# =====Encapsulamento=====
# Ocultar detalhes internos do funcionamento de uma classe
# Proteção de dados
# No Python, a nomeclatura utilizada é apenas uma convenção (_ ou __)
# _ protegido
# __ privado

# =====Abstração=====
# Focar nos aspectos essenciais de um objeto

# =====Herança=====
# Permite que uma nova classe herde os atributos e métodos de uma classe existente
# Classe pai, Classe filho
class Pai:
    def __init__(self, nome):
        self.nome = nome

    def jogar(self):
        print(f"O {self.nome} gosta de jogar.")

class Filho(Pai):

    def mover(self):
        print(f"O {self.nome} gosta de mover.")

filho1 = Filho("Santiago") #Herda da classe pai
filho1.mover()
filho1.jogar() #Herda da classe pai

# =====Polimorfismo=====
# Classes diferentes tenham métodos com o mesmo nome, mas com comportamentos diferentes
class Moto:
    def __init__(self, nome):
        self.nome = nome
    def mover(self):
        print(f"A moto {self.nome} está em movimento.")


class Carro:
    def __init__(self, nome):
        self.nome = nome
    def mover(self):
        print(f"O carro {self.nome} está em movimento.")

carro = Carro("Sandero")
moto = Moto("NMAX")

carro.mover()
moto.mover()
