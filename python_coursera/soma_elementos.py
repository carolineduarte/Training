def soma_elementos(lista):
    n = soma = 0
    tam = len(lista) - 1
    while n <= tam:
        soma = soma + lista[n]
        n = n + 1
    return soma