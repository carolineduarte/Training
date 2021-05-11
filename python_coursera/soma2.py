n = int(input("Digite a quantidade de números a serem somados: "))
soma = 0
i  = 1
while i <= n:
    valor = int(input("Digite um valor a ser somado "))
    soma = soma + valor
    i = i + 1
print("A soma dos valores digitados é: ",soma)