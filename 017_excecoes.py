try:
    numero = int(input())
except ValueError:
    print("Valor atribuido deve ser inteiro")
except Exception as error:
    print(error)
    print(type(error))
else:
    # So será executado se não gerou erro
    print(numero)
finally:
    print("Este bloco sempre será exectuado")


# Gerando exceção

num = int(input("Digite um inteiro positivo: "))

if num <= 0:
    raise ValueError('Numero deve ser maior que 0')