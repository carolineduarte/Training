import math

def é_hipotenusa (n):
    i = 1
    while i < n:
        j = math.sqrt(n**2 - i**2)
        if j - int(j) == 0:
            i = n
            return True
        else:
            i = i + 1
    if i == n:
        return False

def soma_hipotenusas(n):
    soma = 0
    while n >= 1:
        if é_hipotenusa(n):
            soma = soma + n
        n = n - 1
    return soma
