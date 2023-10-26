import sys # Interagir com linha de comando
# https://docs.python.org/3/library/sys.html

print(sys.argv)


if len(sys.argv) != 2:
    #print("O programa deve ser executado como: python nome_arquivo argumento")
    sys.exit("O programa deve ser executado como: python nome_arquivo argumento")

else:
    print(sys.argv[1])


print("Continuação")