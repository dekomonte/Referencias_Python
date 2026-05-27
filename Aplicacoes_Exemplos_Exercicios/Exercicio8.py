# Exercise Cats Everywhere - Given the below class:

class Cat:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats.
gato1 = Cat('Fred', 5)
gato2 = Cat('Feijão', 12)
gato3 = Cat('Amendoeira', 72)
gato4 = Cat('MJ', 5) #Testei com mais
gato5 = Cat('Suelen', 7)
gato6 = Cat('Sushi', 16)


# 2 Create a function that finds the oldest cat.
def maior_gato(gatos):

    gato_mais_velho = None
    idade_gato_mais_velho = 0

    for gato in gatos:
        # print(gato.age)
        if gato.age > idade_gato_mais_velho:
            idade_gato_mais_velho = gato.age

    return idade_gato_mais_velho

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
gatos = [gato1, gato2, gato3, gato4, gato5, gato6]

x = maior_gato(gatos)
print(f"The oldest cat is {x} years old.")
