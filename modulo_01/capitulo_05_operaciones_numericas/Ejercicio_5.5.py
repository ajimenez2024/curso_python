## Ejercicio 5.5

# Construye una calculadora para hallar el area de un cilindro
# 1. usa la funcion input para preguntar los valores de la altura
# el radio
# 2. calcula el area 
# 3. imprime el resultado

import math
radio=input("radio")
radio=float(radio)
altura=input("altura")
altura=float(altura)

area_lateral = 2*math.pi*radio*altura

print("El área lateral del cilindro es: ",area_lateral)


