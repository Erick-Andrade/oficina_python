nomes = ["Joao", "Pedro", "Maria"]
idades = [11, 20, 31]

for i in range(len(nomes)):
    print(f"{nomes[i]} tem {idades[i]}")

print(list(zip(nomes, idades)))
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade}")