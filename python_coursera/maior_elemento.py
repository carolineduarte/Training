def maior_elemento(lista):
    maior = lista[0]
    tam = len(lista) - 1
    n = 1
    while n <= tam:
        if maior < lista[n]:
            maior = lista[n]
        n = n + 1
    return maior