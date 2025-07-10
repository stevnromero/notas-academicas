""""
verdadero = True
falso = False



if(verdadero==True):
    print("hice la tarea")

if(falso==False):
    print("lave los platos")


# ejercicios con operadores de comparacion

nombre1 = "carlos"
nombre2 = "fabio"
nombre3 = "andrés"
edad_carlos = 22
edad_fabio = 15
edad_andrés = 20
hermanos = f"{nombre1}, {nombre2} y {nombre3} son hermanos propios"
print(hermanos)

if(edad_carlos <= edad_fabio):
    print("carlos es mayor que fabio")

elif(edad_fabio >= edad_andrés):
    print("fabio es muy joven")

else:
    print("andres es mayor que fabio")

print(type(hermanos))"""""

# operacion con operadores logicas and, or, not

age = input("how old are you:")
age = int(age)
"""
if(type(age)==int):
    if(age >=18 and age <=40):
        print("puedes pasar")

    elif(age <=17 and age <20):
        print("no puedes entrar")

    elif(age ==40 or age<17):
        print("minimo entras a los 40 años")

    else:
        print("prohibido personas con problemas auditivos")

    print(type(age))"""

if(not(age<=18)):
    print("puedes pasar")