# Ejercicio 5.6

# Calcular el valor de la hipotenusa
# 1. usa la funcion input para preguntar por la longitud de los catetos x y y
# 2. calcula el valor de la hipotenusa
# 3. calcula el valor del angulo entre la hipotenusa y el cateto x
# 4. calcula las funciones trigonométricas seno, coseno y tangente de ese ángulo. 

import math
x=input("ingrese cateto x: ")
x=float(x)
y=input("ingrese cateto y: ")
y=float(y)

hipo=math.sqrt(x**2 + y**2)
print("hipotenusa: ", hipo)
angulo=math.atan(y/x)
seno=math.sin(angulo)
coseno=math.cos(angulo)
tangente=math.tan(angulo)
print("el ángulo es: ", angulo)
print("el seno es: ", seno)
print("el coseno es: ", coseno)
print("la tangente es: ", tangente)

