print("==== Exemplo ====")
for i,char in enumerate('Olaaaaaa'):
    print(i,char)

print("==== Exemplo ====")
for i,char in enumerate([1,6,3,8,2,3,4,23]):
    print(i,char)

print("==== Exemplo ====")
for i,char in enumerate(list(range(10))):
    print(i,char)

print("==== Exemplo ====")
for i,char in enumerate(list(range(10))):
    if char == 5:
        print(f'index de 5: {i}')
