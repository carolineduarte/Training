lista = []
n = 1

while n != 0:
    n = int(input("Digite um número. Para sair, pressione 0: "))
    lista.append(n)
tam = len(lista) - 2

while tam >= 0:
    print(lista[tam], end=", ")
    tam = tam - 1
