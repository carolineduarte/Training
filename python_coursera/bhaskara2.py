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
        print("Há uma única raiz para a equação, a saber: ",x12)
    else:    
        x1 = (-b+raizdelta)/(2*a)
        x2 = (-b-raizdelta)/(2*a)
        print("As raízes da equação são:") 
        print("x1= ",x1)
        print("x2= ",x2)
else:
    raizdeltan = math.sqrt(-delta)
    realx = -b/(2*a)
    imagx = raizdeltan/(2*a)
    print("As raízes da equação são:") 
    print("x1= ",realx,"+",imagx,"i")
    print("x2= ",realx,"-",imagx,"i")