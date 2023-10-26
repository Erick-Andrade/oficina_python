numeros = list(map(int, input().split()))
positivos = list(filter(lambda x: x > 0, numeros))
negativos = list(filter(lambda x: x < 0, numeros))

print(numeros)
print(positivos)
print(negativos)