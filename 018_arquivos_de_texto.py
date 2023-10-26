"""
abre arquivo
faça o que precisa
feche o arquivo

Tipos:
r: read
w: write (sobrescreve)
a: append (adiciona no final)
"""

# Tipo w
arquivo = open("teste.txt", "w")
arquivo.write("Linha1\n")
arquivo.write("Linha2\n")

linhas = [
    "Linha3\n",
    "Linha4\n"
]

arquivo.writelines(linhas)

arquivo.close() # Fechamento

# Tipo a
arquivo = open("teste.txt", "a")
arquivo.write("Não ira sobrescrever\n")
arquivo.close()

## Tipo r
arquivo = open("teste.txt", "r")
print(arquivo.read())
arquivo.close()


# Para não ter que ficar abrindo e fechando, podemos usar a seguinte sintaxe
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha, end="")

with open("teste.txt", "r") as arquivo:
    print(arquivo.readline(), end="")
    print(arquivo.readline(), end="")
    print(arquivo.readline(), end="")
    print(arquivo.readline(), end="")

with open("teste.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha, end="")
