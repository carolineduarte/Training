print("Digite uma sequência de valores terminada por zero.")
produto = 1
valor  = 1
while valor != 0:
    valor = int(input("Digite um valor a ser multiplicado: "))
    if valor != 0:
        produto = produto * valor
print("O produto dos valores digitados é: ",produto)