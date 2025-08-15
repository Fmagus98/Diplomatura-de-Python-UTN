# #########################################
# Ejercicio 3
# Escriba un programa que consulte al usuario por una oración y 
# comente al usuario cuantas veces aparecen todas las vocales 
# considerando minúsculas, mayúsculas y acentos.  
# #########################################

oracion = input("Escribe una oración")
vocales = ['a','á','A','Á','e','é','E','É','i','í','I', 'Í', 'o','ó','O','Ó','u','ú','Ú','U']

def contador(oracion):
    contador = 0
    for letra in oracion:
        if letra in vocales:
            contador += 1
    return contador

print(f"La cantidad de vocales encontradas son {contador(oracion)} vocales")