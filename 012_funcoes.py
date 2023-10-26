
### Retorno de valores

# Sem retorno
def print_value(x):
    print(f"O valor de x e {x}")

resultado = print_value(10)
print(resultado)

# Um valor

def soma(x, y):
    return x + y


print(soma(10, 20))


# Múltiplos valores -> retorna uma tupla

def calculo(x, y):
    return x+y, x-y, x*y, x/y


resultado = calculo(10, 2)
soma1, sub, mult, div = calculo(50, 10)
soma1, *_ = calculo(50, 10)

print(resultado)
print(soma1, sub, mult, div)

#### global scope
x = "Teste"
def myFunction():
    # local scopoe
    x = "Mudei"
    print(x)

myFunction()
print(x)


# Pegando (ou criando) uma variável global e um escopo local
x = "Teste"
def myFunction():
    global new_variable # nova variável global
    global x # pegando uma variável global
    # Ou simplemeste
    # global new_variable, x
    x = "Mudei"
    new_variable = 10
    print(x)

myFunction()
print(x)
print(new_variable)


##### Função anônima (lambda function)
# lambda parâmetros : expressão

funcao_anonima = lambda x: x + 2
soma = lambda x, y: x + y
print(funcao_anonima(3))
print(soma(10, 20))

#### Parâmetros

# Padrão

def soma(x, y=10):
    return x + y

print(soma(10))
print(soma(10, 0))

# * -> empacota todos os argumentos enviados em uma variável do tipo tupla (normalmente chamado de *args)
def teste(*args): # Recebe `*args` como parâmetro
    print(args) # Imprime `args`
    print(type(args))

teste(1, 2, 3)
teste(4, 5)

# ** -> empacota todos os argumentos enviados em uma variável do tipo dicionario (normalmente chamado de **kwargs)

def teste(**kwargs): # Recebe `**kwargs` como parâmetro
    print(kwargs) # Imprime `kwargs`

teste(arg1="valor1", arg2="valor2")

## Podemos passar funções como parâmetros
# Funções de Ordem Superior (Higher-Order Functions)
# recebem uma função como parâmetro ou retornam uma função

def converter(x, fun):
    return fun(x)

print(converter("Ola Mundo", str.lower))
print(converter("Ola Mundo", str.upper))


##### Boas práticas
### docstring: explica o propósito da função, seus parâmetros e seu valor de retorno

def calculo(x, y):
    """
    Calcula a soma dos quadrados de x e y

    Parâmetros:
    x (int): O primeiro número
    y (int): O segundo número

    Retorna:
    int: A soma dos quadrados de x e y
    """
    resultado = x ** 2 + y ** 2
    return resultado

print(calculo(5, 2))

### Type Hint ou Type Annotation

def imprime(s: str) -> None:
    print(s)

def calculo(x:int, y:int) -> int:
    """
    Calcula a soma dos quadrados de x e y

    Parâmetros:
    x (int): O primeiro número
    y (int): O segundo número

    Retorna:
    int: A soma dos quadrados de x e y
    """
    resultado = x ** 2 + y ** 2
    return resultado

print(calculo(5, 2))
