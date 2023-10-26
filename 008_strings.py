# String de uma linha

formasString = "Hello World"
formasString2 = 'Hello World'

# String de múltiplas linhas
formasString3 = """Hello
World
"""
formasString4 = '''Hello
World
'''


print(type(formasString))
print(type(formasString2))
print(type(formasString3))
print(type(formasString4))


##############  Strings são listas
print(formasString[0])

# Em python, tem-se index negativo para qualquer estrutura indexada
"""
string: Hello
index:  01234
        54321 (sendo negativo)
"""
print(formasString[0], formasString[-len(formasString)])
print(formasString[len(formasString)-1], formasString[-1])



############## String são imutáveis

teste = "Teste"
# teste[0] = "A"


############## Percorrendo um string

nome = input("Digite um nome: ")
for letra in nome:
    print(letra)


############## Verificando se uma string está em outra

frase = "Hello World"
if "Hello" in frase:
    print("Hello esta na frase")

if "Hi" in frase:
    print("Hi esta na frase")

# Podemos verificar se a string não está em outra (apenas utilizando o not)

if "Hi" not in frase:
    print("Hi não esta na frase")


############## Slicing Strings - pegar uma parte da string

frase = "Hello, World!"

"""
[i:e] -> retorna uma string com os caracteres dos índices de i até e-1
[:e] -> retorna uma string com os caracteres dos índices 0 até e-1
[i:] -> retorna uma string com os caracteres dos índices i até o final
"""
print(frase[0:5])
print(frase[:10])
print(frase[1:])


# Podemos utilizar índices negativos também
print(frase[-5:-2])


############## Caracteres de escape
"""
\n -> quebra de linha
\t -> tabulação
"""

print("\\ \'Ignorando aspas\' \n\n")
print("\tOii")

############## Métodos

### Retornando a string alterada

s1 = "hElLo WORLD"

upper = s1.upper()
lower = s1.lower()
title = s1.title()
replace = s1.replace("hElLo", "Hi")


print(s1)
print(upper)
print(lower)
print(title)
print(replace)

### string -> list
s1 = "10, 20, 30"
l1 = s1.split()
l2 = s1.split(",")

print(l1, type(l1))
print(l2, type(l2))

s2 = "10.....1000"
print(s2.split("....."))


### Removendo caracteres do começo e/ou fim
# strip() -> remove do começo e fim
# rstrip() -> remove do final
# lstrip() -> remove do começo

s1 = "                  Teste                   "
s2 = "-------Teste------"

strip1 = s1.strip()
strip2 = s2.strip('-')

print(s1, len(s1))
print(strip1, len(strip1))

print(s2, len(s2))
print(strip2, len(strip2))
