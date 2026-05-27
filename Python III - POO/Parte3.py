#OOP

#Example
class PersonWorker:

    #Class Object Attribute
    ativo = True
    def __init__(self, nome, idade):
        if PersonWorker.ativo:
            #attribute
            self.nome = nome
            self.idade = idade

    def shout(self):
        print(f'Ola, meu nome é: { self.nome }')

    def run(self, hello):
        print(f'Run, { self.nome }')

person2 = PersonWorker("Tasha", 44)
person2.shout()
person2.run("Aaaaaaaa...") #A classe pede um argumento mas não usa


