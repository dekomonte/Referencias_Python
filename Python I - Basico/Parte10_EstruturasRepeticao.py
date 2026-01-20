#==========Estruturas de Repeticao==========
#WHILE -> Executa ações enquanto uma condição for verdadeira

#Exemplo 1
print("===== Exemplo 1 =====")
condicao = True
while condicao:
    print(1)
    print(2)
    print(3)
    condicao = False

#Exemplo 2
print("===== Exemplo 2 =====")
cont = 0
while cont < 15:
    print(f"Bora tubarões! + {cont}")
    cont+=1
    
#Exemplo 3
print("===== Exemplo 3 =====")
i = 0
while i < 5:
    print(i)
    if i == 3:
        print("Vou sair do loop com break, i não vai chegar no 5")
        break #Sai do loop antes da condição ser ficar falsa
    i+=1
    
#Exemplo 4
print("===== Exemplo 4 =====")
i = 0
while i < 5:
    i+=1
    if i == 3:
        print("Vou entrar aqui e retornar para o início do loop")
        continue #Pula para a próxima iteração
    print(i)
    

#Exemplo 5
print("===== Exemplo 5 =====")
linhas=1
while linhas < 5:
    colunas=1
    while colunas < 5:
        print(f"linha:{linhas} e coluna:{colunas}")
        colunas+=1
    linhas+=1
    
