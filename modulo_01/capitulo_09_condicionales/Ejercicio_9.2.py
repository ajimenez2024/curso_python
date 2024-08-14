##Ejercicio 9.2

# Ingresar su nombre y luego verifique si el nombre ingresado tiene más de 5 letras. 

nombre=input("escriba un nombre: ")
largo=len(nombre)


if largo > 5:
    print("el nombre tiene más de 5 letras")
else:
    print("el nombre tiene 5 letras o menos")
