#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
print("----- ejercicio 1 -----")
print("")

age = int(input("Ingrese su edad: "))
if age > 18:
    print("Es mayor de edad")
elif age == 18:
    print("Tiene 18 años, por lo tanto es mayor de edad") # la consigna dice mayor a 18, no 18 o mas. Pero me parecio correcto agregar este caso.
else:
    print("Es menor de edad")

print("")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar elmensaje “Desaprobado”.

print("----- ejercicio 2 -----")
print("")
score = int(input("Ingrese su nota: "))
if score >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print("")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa unnúmero par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
print("----- ejercicio 3 -----")
print("")
number= int(input("Ingrese un número: "))

if number % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print("")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

print("----- ejercicio 4 -----")
print("")
age = int(input("Ingrese su edad: "))
if age < 0:
    print("Edad invalida")
elif age < 12:
    print("Niño/a")
elif age >= 12 and age < 18:
    print("Adolescente")
elif age >= 18 and age < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
print("")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
print("----- ejercicio 5 -----")
print("")
password = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("")

#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma:

print("----- ejercicio 6 -----")
print("")
import random
from statistics import mode, median, mean
random_numbers = [random.randint(1, 100) for _ in range(50)]

mode_value = mode(random_numbers)
median_value = median(random_numbers)
mean_value = mean(random_numbers)

if mean_value > median_value and median_value > mode_value:
    print("Sesgo positivo")
elif mean_value < median_value and median_value < mode_value:
    print("Sesgo negativo")
elif mean_value == median_value and median_value == mode_value:
    print("No hay sesgo")
else:
    print("No se puede determinar un sesgo")
print(f"Numeros aleatorios: {random_numbers}")
print(f"Moda: {mode_value}, Mediana: {median_value}, Media: {mean_value}")
print("")
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
print("----- ejercicio 7 -----")
print("")
vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user_string = input("Ingrese una frase o palabra: ")
for i in range(len(vowels_list)):
    if user_string[-1] == vowels_list[i]:
        user_string += "!"
        break
print(user_string)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3dependiendo de la opción que desee. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla
print("----- ejercicio 8 -----")
print("")
name = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1. Convertir el nombre a mayúsculas.")   
print("2. Convertir el nombre a minusculas.")
print("3. Capitalizar el nombre (primera letra en mayuscula y el resto en minuscula).")
option = int(input("Ingrese 1, 2 o 3: "))
if option == 1:
    name = name.upper()
    print(name)
elif option == 2:
    name = name.lower()
    print(name)
elif option == 3:
    name = name.title()
    print(name)
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

print("")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla
print("----- ejercicio 9 -----")
print("")
magnitude = float(input("Ingrese la magnitud del terremoto: "))
if magnitude < 3:
    print("Muy leve (imperceptible)")
elif magnitude >= 3 and magnitude < 4:
    print("Leve (ligeramente perceptible)")
elif magnitude >= 4 and magnitude < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitude >= 5 and magnitude < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitude >= 6 and magnitude < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitude >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Magnitud inválida")
print("")

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

print("----- ejercicio 10 -----")
print("")

hemisphere = input("Ingrese en cuál hemisferio se encuentra (N/S): ")
month = int(input("Ingrese el mes del año (1-12): "))
day = int(input("Ingrese el día del mes (1-31): "))

if (month < 1 or month > 12) or (day < 1 or day > 31):
    print("Fecha inválida")
    hemisphere = "X" #para que no entre en la siguiente condicion


if hemisphere.upper() == "N" or hemisphere.upper() == "S":


    if ( month >= 3 and month <= 6):

        if month == 3 and day < 21:
            if hemisphere.upper() == "N":
                print("Invierno")
            else:
                print("Verano")
        elif month == 6 and day > 20:
            if hemisphere.upper() == "N":
                print("Verano")
            else:
                print("Invierno")
        else:
            if hemisphere.upper() == "N":
                print("Primavera")
            else:
                print("Otoño") 


    elif ( month >= 6 and month <= 9):
        
        if month == 6 and day < 21:
            if hemisphere.upper() == "N":
                print("Primavera")
            else:
                print("Otoño")
        elif month == 9 and day > 20:
            if hemisphere.upper() == "N":
                print("Otoño")
            else:
                print("Primavera")
        else:
            if hemisphere.upper() == "N":
                print("Verano")
            else:
                print("Invierno")
    elif ( month >= 9 and month <= 12):

        if month == 9 and day < 21:
            if hemisphere.upper() == "N":
                print("Verano")
            else:
                print("Invierno")
        elif month == 12 and day > 20:
            if hemisphere.upper() == "N":
                print("Invierno")
            else:
                print("Verano")
        else:
            if hemisphere.upper() == "N":
                print("Otoño")
            else:
                print("Primavera")


    else: 

        if month == 12 and day >= 21:
            if hemisphere.upper() == "N":
                print("Invierno")
            else:
                print("Verano")
        elif month == 3 and day <= 20:
            if hemisphere.upper() == "N":
                print("Invierno")
            else:
                print("Verano")
        else:
            if hemisphere.upper() == "N":
                print("Invierno")
            else:
                print("Verano")
