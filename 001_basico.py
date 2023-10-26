#### Sintaxe básica

# identação serve para indicar um bloco de código
# usa-se ":" no lugar de "{}"
if 5 > 2:
    # A identação, normalmente, são múltiplos de 4
    print("Five is greater than two")

# Não é uma boa prática
if 5 > 2:
    print("Oiiii")
if 5 > 2:
 print("AAA")

# Não se pode ter identações diferentes no mesmo bloco de código
"""
if 5 > 2:
    print("4 espaços")
        print("8 espaços")
"""

#### Variáveis 

"""
---- Regras de nomenclatura
Pode começar com letra ou underscore (_)
Pode conter caracters alpha numéricos e underscore (a-z, A-Z, 0-9 e _)
Não pode ser uma palavra reservada do python (keywords, ex: if, def, for, else, ...)
"""

## tem tipagem dinâmica

a = "Oi"
print(type(a))
a = 10
print(type(a))
a = 10.4
print(type(a))
a = True
print(type(a))

## Atribuição de várias variáveis com valores iguais

a = b = c = 10
print(a)
print(b)
print(c)

## Unpacking

# Mesmo número de valores e variáveis
a, b, c = 10, 20, 30
d, e, f = [23, 32, 53]

print(a, b, c, d, e, f)

# Número diferente de valores e variáveis: Uso de *
*a, b = 10, 20, 30, 40
print(a, b)

# _ -> serve para ignorar
a, _, _, c = 10, 20, 30, 40
print(a, c)

## Boa prática: Type Hint ou Type Annotation
# Mas, a linguagem continuacom tipagem dinâmica

# Tipos básicos: nome_variável: tipo_variável = valor_variável
idade: int = 12
print(idade)
print(type(idade))

idade = 1.232
print(idade)
print(type(idade))

# Coleções: nome_variável: tipo_estrutura [ tipo_variável_armazenada ]

lista: list[int] = [1, 2, 3, 4, 5]
dicionario: dict[str, int] = {"Joao": 16}

# Classe

class MinhaClasse:
    pass

obj: MinhaClasse = MinhaClasse()
# Podemos utilizar o "ou": |

lista: list[int | str] = [1, "10", 10, 30]


#### Input e output

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

# .format()

print("{} + {} = {}".format(x, y, x + y))
print("{0} + {1} = {2}".format(x, y, x + y))
print("{2} + {0} = {1}".format(x, y, x + y))
print("{0} + {0} = {1}".format(x, x+x))
print("{} / {} = {:.2f}".format(x, y, x / y))


# f string
print(f"{x} + {y} = {x+y}")
print(f"{x} / {y} = {x/y:.2f}")

# r string: usado para ignorar todos os caracteres especiais em uma string
path = r"C:\Users"

## parâmetros

# end (default é "\n")
print("Ola", end=" ")
print("Mundo!")

print("Ola", end="\t")
print("Mundo")

# sep (default é " ")
print("Ola", "Mundo")
print("Ola", "Mundo", sep="-------")


# Input de vários valores

numeros = input().split()
print(numeros)