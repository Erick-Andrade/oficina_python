nota = float(input())

if nota >= 7:
    print("Aprovado")
elif 5 <= nota < 7: # Poderia se resumir a nota >= 5
    print("Recuperação")
else:
    print("Reprovado")


"""
Operadores de comparação: >, >=, ==, !=, <, <=
Operadoers lógicos: and, or e not
"""
a = 5
if a == "5":
    print("Expressão verdadeira")
else:
    print("Expressão não e verdadeira")

if a == 5:
    print("Expressão verdadeira")
else:
    print("Expressão não e verdadeira")


# While

v = 0 
while v < 5:
    print(v)
    v += 1


numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(0, 6, 1):
    print(num)

r = range(0, 6, 1)
print(type(r))
print(type(list(r)))

numbers = [1, 2, 3, 4]
for indice, num in enumerate(numbers):
    print(indice, num)