import os # Iteragir com o sistema operacional

pasta_atual = os.getcwd()
print(pasta_atual)

print(os.listdir())
os.mkdir("teste")
print(os.listdir())

os.chdir(r"C:\Users")
print(os.getcwd())


os.system("cls") # Podemos utilizar um comando do terminal

# Trabalhar com caminhos os.path
caminho = os.path.join("pasta", "subpasta", "teste.txt") 
# Ao executar esse código em um ambiente Windows será impresso "pasta\subpasta\teste.txt". Já no Linux, será impresso "pasta/subpasta/teste.txt"
print(caminho)