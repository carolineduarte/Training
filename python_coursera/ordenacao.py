print("Este programa verifica se a ordenação de três números inteiros é ou não crescente.")
a=int(input("Digite o primeiro número inteiro: "))
b=int(input("Digite o segundo número inteiro: "))
c=int(input("Digite o terceiro número inteiro: "))
if (a < b) and (b < c):
    print("crescente")
else:
    print("não está em ordem crescente")