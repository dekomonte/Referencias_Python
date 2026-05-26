#OOP
#Instantiate -> Calling the class to create an object

#Example
class PersonagemJogador:

    def __init__(self, nome):
        self.nome = nome

    def run(self):
        print('run')

jogador1 = PersonagemJogador("Elfo")
jogador2 = PersonagemJogador("Mago")

print(jogador1.nome)
jogador1.run()

print(jogador2.nome)
jogador2.run()

#Example
class Person:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def greet(self):
        print(f'Ola, meu nome é: { self.nome }')

person1 = Person("Joana", 65)
person1.greet()

