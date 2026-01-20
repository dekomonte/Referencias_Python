#==========Estruturas de Repeticao==========
#WHILE -> Executa ações enquanto uma condição for verdadeira

#Exemplo 1
condicao = True
while condicao:
    print(1)
    print(2)
    print(3)
    condicao = False

#Exemplo 2
cont = 0
while cont < 17:
    print("Saudades da minha amiga")
    print(cont)
    cont+=1
    
#Exemplo 3
i = 0
while i < 5:
    print(i)
    if i == 3:
        print("Vou sair do loop com break, i não vai chegar no 5")
        break #Sai do loop antes da condição ser ficar falsa
    i+=1


#Operadores de atribuição
#= += -= *= /= //= **= %=
