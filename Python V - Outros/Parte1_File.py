meu_arquivo = open("Parte1_File.txt")

#Arquivos usam a ideia de cursor, que indica a posição atual de leitura no arquivo.
print("Exemplo Cursor")
print(meu_arquivo.read())
print(meu_arquivo.read())
print(meu_arquivo.read())


meu_arquivo.seek(0)
print(meu_arquivo.read())

#Cursor fica se movendo a cada leitura de linha
print("Exemplo Readline")
meu_arquivo.seek(0)
print(meu_arquivo.readline())
print(meu_arquivo.readline())
print(meu_arquivo.readline())

print("Exemplo Readlines")
meu_arquivo.seek(0)
print(meu_arquivo.readlines())

meu_arquivo.close()
