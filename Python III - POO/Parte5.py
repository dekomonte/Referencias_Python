#OOP - Dunder Methods

#Métodos especiais que começam e terminam com __

#Servem para você dizer ao Python como os seus objetos 
#customizados devem se comportar quando interagem com 
#operações nativas da linguagem

#Example
class Brinquedo():

    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'cor: {self.color}, idade: {self.age}'

    def __len__(self):
        return 5

brinquedo = Brinquedo("azul", 18)
brinquedo2 = Brinquedo("verde", 0)

print(brinquedo.__str__())
print(str(brinquedo))

print(len(brinquedo))
