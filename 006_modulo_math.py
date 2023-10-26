# Módulo: um arquivo
# Pacote: junção de módulos relacionados
# Biblioteca: coleção de pacotes

# Todas elas, nos permite importar funcionalidades feita por outros (ou do próprio python)


import math # módulo

numero = 3.47
print(math.ceil(numero))
print(math.floor(numero))

numero = 4
print(math.factorial(numero))
print(math.sqrt(numero))


num1 = 4
num2 = 5
print(math.gcd(num1, num2)) # mdc(num1, num2)


## ** pode retorna inteiro
print(2 ** 5) 
print(math.pow(2, 5))


print(2.5 ** 5)
print(math.pow(2.5, 5))



# Se caso precisar apenas de uma função ou especifica podemos, importar assim

from math import ceil

print(ceil(10.312312))