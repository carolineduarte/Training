lista = []
n = int(input("Digite um número: "))
while n != 0:
    lista.append(n)
    n = int(input("Digite um número: "))

i = len(lista)-1
while i >= 0:
    print(lista[i])
    i = i - 1 