# ########################################################################################
# Ejercicio 5
# Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
# función, de forma que la operacion se realice dentro de la misma. 

# Presente el resultado en la terminal
# ########################################################################################

# ################################################################################################
# Ejercicio 3(unidad 1):
# Escriba un programa que solicite el
# perímetro. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# L = 2 · π · r
# L = Longitud de perímetro
# π = Número pí igual a 3.1416
# r = Radio
# ################################################################################################

def calcular_perimetro(n):
    PI = 3.1426
    l = 2 * 3.1416 * n
    print("El perímetro del círculo es: ", l)
    
radio = float(input("Ingrese el radio: "))
calcular_perimetro(radio)

# ################################################################################################
# Ejercicio 4:
# Escriba un programa que solicite el radio de una circunferencia y permita calcular el
# área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# 𝐴 = 𝜋. 𝑟ଶ
# A = Área
# ################################################################################################

def calcular_area(n):
    PI = 3.1426
    area = PI * (radio ** 2)
    print("El área del círculo es: ", area)

radio = float(input("Ingrese el radio:"))
calcular_area(radio)

# ################################################################################################
# Ejercicio 5:
# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
# editor el valor incrementado en un 10%.
# ################################################################################################

def incremetar_valor(n):
    valor_incrementado = n + (n * 0.1)
    print("El valor incrementado en un 10% es: ", valor_incrementado)
    
valor = int(input("Ingrese un valor:"))
incremetar_valor(valor)