import math
print("Este programa calcula as raízes de uma equação quadrática: ax2+bx+c ")
a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))
delta = b**2-4*a*c
if delta >= 0:
    raizdelta = math.sqrt(delta)
    if delta == 0:
        x12 = (-b)/(2*a)
        print("a raiz desta equação é",x12)
    else:    
        x1 = (-b+raizdelta)/(2*a)
        x2 = (-b-raizdelta)/(2*a)
        if x1 < x2:
            print("as raízes da equação são",x1,"e",x2)
        else:
             print("as raízes da equação são",x2,"e",x1)
else:
    print("esta equação não possui raízes reais")     