# ################################################################################################
# Ejercicio 1:
# Cree un programa que tome tres valores por consola multiplique el primero por el segundo
# y le sume el tercero. Presente el resultado en la terminal
# ################################################################################################
valor1 = float(input("Ingresa un numero: "))
valor2 = float(input("Ingresa un numero: "))
valor3 = float(input("Ingresa un numero: "))

resultado = (valor1 * valor2) + valor3

print("El resultado es: ", resultado)

# ################################################################################################
# Ejercicio 2:
# Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
# pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
# son múltiplos de dos.
# ################################################################################################

import sys
print (sys.argv) 
print (f"{int(sys.argv[1])} es par?\n", "Si" if int(sys.argv[1])%2 == 0 else "No") 
print (f"{int(sys.argv[2])} es par?\n", "Si" if int(sys.argv[1])%2 == 0 else "No") 
print (f"{int(sys.argv[3])} es par?\n", "Si" if int(sys.argv[1])%2 == 0 else "No") 

# ################################################################################################
# Ejercicio 3:
# Escriba un programa que solicite el
# perímetro. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# L = 2 · π · r
# L = Longitud de perímetro
# π = Número pí igual a 3.1416
# r = Radio
# ################################################################################################

radio = float(input("Ingrese el radio:"))
PI = 3.1426
l = 2 * 3.1416 * radio
print("El perímetro del círculo es: ", l)


# ################################################################################################
# Ejercicio 4:
# Escriba un programa que solicite el radio de una circunferencia y permita calcular el
# área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# 𝐴 = 𝜋. 𝑟ଶ
# A = Área
# ################################################################################################
radio = float(input("Ingrese el radio:"))
PI = 3.1426
area = PI * (radio ** 2)
print("El área del círculo es: ", area)

# ################################################################################################
# Ejercicio 5:
# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
# editor el valor incrementado en un 10%.
# ################################################################################################
valor = int(input("Ingrese un valor:"))
valor_incrementado = valor + (valor * 0.1)
print("El valor incrementado en un 10% es: ", valor_incrementado)
