# #########################################
# Ejercicio 2
# Escriba un programa que consulte al usuario por una oración y 
# comente al usuario cuantas veces aparece la letra “a”. 
# #########################################

oracion = input("Escribe una oración: ").lower()
print(f"letras 'a' encontradas: {oracion.count('a')}")