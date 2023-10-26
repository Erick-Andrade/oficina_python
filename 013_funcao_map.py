# Executar uma função para cada elemento de um iterable
# map(funcao_para_aplicar, iterable)

def quadrado(x):
    return  x ** 2

lista = [1, 2, 3, 4, 5]
ao_quadrado = list(map(quadrado, lista))
ao_quadrado2 = list(map(lambda x: x ** 2, lista))

print(ao_quadrado)
print(ao_quadrado2)


entradaInteiros = list(map(int, input().split()))
a, b = list(map(int, input().split()))
print(type(a), type(b))