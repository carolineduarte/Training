def remove_repetidos(lista):
    n = 0
    while n <= len(lista) - 1:
        i = 0
        while i <= len(lista) - 1:
            if i != n and lista [n] == lista [i]:
                del lista[i]
            i = i + 1
        n = n + 1
    list.sort(lista)
    return lista 