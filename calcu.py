print("--Calculadora--")
print("1.-Suma (a+b)")
print("2.-Resta (a-b)")
print("3.-Multiplicacion (a*b)")
print("4.-Division (a/b)")
opc=int(input("Ingresa el numero de la operaciom que deseas realizar"))
a=int(input("Ingresa un número a"))
b=int(input("Ingresa un número b"))


def suma(a,b):
    res=a+b
    return res

def resta(a,b):
    res=a-b
    return res

def multi(a,b):
    res=a*b
    return res

def div(a,b):
    if b==0:
        print("b debe ser un numero diferente de 0")
    else:
        res=a/b
    return res
print("El resultado es:")
if opc==1:
    print(suma(a,b))
elif opc==2:
    print(resta(a,b))
elif opc==3:
    print(multi(a,b))
elif opc==4:
    print(div(a,b))    
else:
    print("Ingresaste un valor ewuivocado")
