"""
Conjuntos da matemática, sendo assim:
    - não podem ser duplicados
    - é possível realizar operações como união e interseção
"""

# Podemos apenas adicionar ou remover
s1 = {1, 2, 3}
print(s1)
print(type(s1))


s1.add(1)
s1.add(1)
s1.add(1)
s1.add(1)
s1.add(1)
s1.add(1)
print(s1)

# Podemo utilizar em:

lista = [1, 2, 2, 3, 4, 4, 4, 4, 5]
lista_sem_repeticao = list(set(lista))
print(lista_sem_repeticao)

# Criar um set vazio

s1 = set()
print(type(s1))
s1 = {}
print(type(s1))


# Remover

s1 = {1, 2, 3}
s1.remove(1)
#s1.remove(100)

s1.discard(2)
s1.discard(100) # Não gera erro

print(s1)

# Percorrer

s1 = {1, 2, 3, 4, 5, 6, 7}
for elem in s1:
    print(elem)


print(1 in s1)
print(100 in s1)


### Operações

s = {1, 2}
t = {2, 3}

# União
print(s | t)
print(s.union(t))

# Intersecção

print(s & t)
print(s.intersection(t))


# Diferença

print(s - t)
print(s.difference(t))