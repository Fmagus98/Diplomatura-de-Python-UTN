# #########################################
# Ejercicio 4
# Escriba un programa que solicite la edad de la persona 
# e imprima todos los años que la persona ha cumplido. 
# #########################################
edad = int(input("Ingrese su edad: "))
anio_actual = 2025
for i in range(anio_actual - edad + 1,anio_actual):
    print(i + 1)
    
# Le añadí un +1 en el range anio_actual - edad porque mi fecha de nacimiento no la cuento