# par: chave / valor
# chaves tem valor único
# chaves podem ser do tipo: int, float, string, ...


dicionario = {}
print(type(dicionario))


dicionario = {
    "Joao": "joao@gmail.com",
    "Maria": "maria@gmail.com",
    "Davi": "davi@gmail.com"
}

print(dicionario["Joao"])
#print(dicionario["Marcos"])

print(dicionario.get("Marcos"))
print(dicionario.get("Marcos", "Usuario não encontrado"))



# Criar ou alterar

dicionario["Joao"] = "jogoModifiquei@gmail.com"
dicionario["Clara"] = "clara@gmail.com"

print(dicionario)

# Remover

del dicionario["Joao"]
print(dicionario.pop("Joao", "Nao encontrado"))
print(dicionario)


### Percorrendo

for chave in dicionario:
    print(chave, dicionario[chave])

for chave in dicionario.keys():
    print(chave)


for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(chave, valor)


### Verificando a existência

# Chaves

print("Maria" in dicionario)
print("Maria" in dicionario.keys())

# Valores
print("maria@gmail.com" in dicionario.values())

### Compreensão de Dicionários

aoQuadrado = {chave:chave*chave for chave in range(1, 10)}
paridade = {
    "par" if chave % 2 == 0 else "impar"
    for chave in range(1, 11)
}

print(aoQuadrado)
print(paridade)