# ##########################################
# Ejercicio 1
# Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo. 
# #########################################

# ########################################################################################
# Ejercicio 1 (unidad 2)
# Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
# pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
# son múltiplos de dos. Utilice la estructura if/else
# ########################################################################################
import sys
print (sys.argv) 
for i in range(1, len(sys.argv)):
    if int(sys.argv[i]) % 2 == 0:
        print(f"El número {sys.argv[i]} es par")