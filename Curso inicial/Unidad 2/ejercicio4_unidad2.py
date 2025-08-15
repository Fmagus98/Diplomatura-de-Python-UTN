# ########################################################################################
# Ejercicio 4
# Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
# fecha de jubilación, presente en la terminal el mensaje "Ya está en edad de jubilarse", 
# en caso contrario que presente “Aun está en edad de trabajar
# ########################################################################################
import datetime

edad_jubilacion = 65
dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
anio = int(input("Ingrese su año de nacimiento: "))
fecha_nacimiento = datetime.datetime.strptime(f"{anio}-{mes}-{dia}", "%Y-%m-%d")

hoy = datetime.datetime.now()
edad = hoy.year - fecha_nacimiento.year

if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

if edad >= edad_jubilacion:
    print(f"Ya está en edad de jubilarse")
else:
    print(f"Aun está en edad de trabajar")