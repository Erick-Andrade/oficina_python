from datetime import datetime
# https://docs.python.org/pt-br/3/library/datetime.html

data = datetime(2023, 10, 23)
data_em_br = data.strftime("%d/%m/%Y")


print(data)
print(data_em_br)


data_string = input()
data = datetime.strptime(data_string, "%d/%m/%Y")
print(data)


data_atual = datetime.now()
print(data_atual)