lista = []
print(type(lista))

lista = [1, 3, 5, 7]
print(type(lista))

lista = [True, 1, 3.23, "Alo"]
print(type(lista))


### Método

lista = [20, 30, 40, 50]
lista.append(10)
print(lista)

lista.insert(1, 100000)
print(lista)

del lista[0]
print(lista)

ultimo = lista.pop()
print(ultimo)

lista.remove(30)
print(lista)

### Mutável
lista[0] = 132312
print(lista)



print(lista[0:2])
print(lista[::2]) # Incrementando de dois em dois
print(lista[::-1]) #Invertendo


############# Compreensão de Listas
lista = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
aoQuadrado = [valor * valor for valor in lista]
positivos = [valor for valor in lista if valor > 0]
paridade = [f"{valor} é par" if valor % 2 == 0 else f"{valor} é ímpar" for valor in lista]

"""
Equivalente a:

aoQuadrado = []
for val in lista:
    aoQuadrado.append(val*val)
"""
print(lista)
print(aoQuadrado)
print(positivos)
print(paridade)

############## Copia de list

s1 = [10, 20, 3 ]
s2 = s1
print(s1, s2)
s1.append(2300)
print(s1, s2)