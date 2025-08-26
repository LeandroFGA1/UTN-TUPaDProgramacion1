#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("ejercicio 1")
print("")
print("Hola Mundo!")
print("")
print("////////////////////////////")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
print("ejercicio 2")
print("")

user_name = input(" ingresa tu nombre: ")
print(f"Hola {user_name}!")

print("")
print("////////////////////////////")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
print("ejercicio 3")
print("")

first_name = input(" ingresa tu nombre: ")
last_name = input(" ingresa tu apellido: ")
age = input(" ingresa tu edad: ")
residence = input(" ingresa tu lugar de residencia: ")
print(f"Soy {first_name} {last_name}, tengo {age} años y vivo en {residence}.")

print("")
print("////////////////////////////")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("ejercicio 4")
print("")

pi = 3.1415926535
radius = float(input(" ingresa el radio del círculo: "))
area = pi * (radius ** 2)
perimeter = 2 * pi * radius
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimeter}")

print("")
print("////////////////////////////")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
print("ejercicio 5")
print("")

seconds = int(input(" ingresa una cantidad de segundos: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{seconds} segundos equivalen a {hours} horas, {minutes} minutos y {remaining_seconds} segundos.")

print("")
print("////////////////////////////")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("ejercicio 6")
print("")

number = int(input(" ingresa un número: "))
print(f"Tabla de multiplicar del {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("")
print("////////////////////////////")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("ejercicio 7")
print("")

number_one = int(input(" ingresa el primer número entero distinto de 0: "))
number_two = int(input(" ingresa el segundo número entero distinto de 0: "))
if number_one != 0 and number_two != 0:
    addition = number_one + number_two
    subtraction = number_one - number_two
    multiplication = number_one * number_two
    if number_two != 0:
        division = number_one / number_two
    else:
        division = "No se puede dividir por cero"
    
    print(f"Suma: {addition}")
    print(f"Resta: {subtraction}")
    print(f"Multiplicación: {multiplication}")
    print(f"División: {division}") 
else:
    print("Ambos números deben ser distintos de 0.")

print("")
print("////////////////////////////")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("ejercicio 8")
print("")

height = float(input(" ingresa tu altura en metros: "))
weight = float(input(" ingresa tu peso en kilos: "))
imc = weight / (height ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

print("")
print("////////////////////////////")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("ejercicio 9")
print("")

celsius = float(input(" ingresa una temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

print("")
print("////////////////////////////")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("ejercicio 10")
print("")

number_one = float(input(" ingresa el primer número: "))
number_two = float(input(" ingresa el segundo número: "))
number_three = float(input(" ingresa el tercer número: "))
average = (number_one + number_two + number_three) / 3
print(f"El promedio de los números ingresados es: {average}")

print("")
print("////////////////////////////")
