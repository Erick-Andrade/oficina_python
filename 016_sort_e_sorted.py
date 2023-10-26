L = [3, 2, 1, 4, 5]


# Sorted: não muda a lista (retorna)

ordem = sorted(L)
print(L)
print(ordem)


ordem = sorted(L, reverse=True)
print(L)
print(ordem)
# Sort: muda a lista

L.sort()
print(L)

L.sort(reverse=True)
print(L)
