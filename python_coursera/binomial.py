def fatorial(n):
    i = fat = 1
    if n == 0:
        fat = 1 
    else:
        while i <= n:
            fat = fat * i
            i = i+ 1
    return fat

print("Programa para cálculo de número binomial n de classe k")
n = int(input("Digite o valor de n: "))
while n < 0:
    n = int(input("Digite um valor válido para n: "))
k = int(input("Digite o valor de k: "))
while k > n or k < 0:
    k = int(input("Digite um valor válido para k: "))
binomial = int(fatorial(n)/(fatorial(k) * fatorial(n-k)))
print("O coeficiente binomial de número n =",n,"na classe k =",k,"é binomial =",binomial)
