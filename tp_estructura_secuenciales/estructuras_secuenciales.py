## 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("ejercicio 1")
print("")
print("Hola Mundo!")
print("")
print("////////////////////////////")

##2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
##el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
##por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
##realizar la impresión por pantalla.
print("ejercicio 2")
print("")

nombre = input(" ingresa tu nombre: ")
print(f"Hola {nombre}!")

print("")
print("////////////////////////////")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
print("ejercicio 3")
print("")

nombre = input(" ingresa tu nombre: ")
apellido = input(" ingresa tu apellido: ")
edad = input(" ingresa tu edad: ")
lugar_residencia = input(" ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

print("")
print("////////////////////////////")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("ejercicio 4")
print("")

pi =3.1415926535
radio = float(input(" ingresa el radio del círculo: "))
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

print("")
print("////////////////////////////")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla acuántas horas equivale
print("ejercicio 5")
print("")

segundos = int(input(" ingresa una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

print("")
print("////////////////////////////")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("ejercicio 6")
print("")
numero = int(input(" ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print("")
print("////////////////////////////")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("ejercicio 7")
print("")
numero_uno = int(input(" ingresa el primer número entero distinto de 0: "))
numero_dos = int(input(" ingresa el segundo número entero distinto de 0: "))
if numero_uno != 0 and numero_dos != 0:
    suma = numero_uno + numero_dos
    resta = numero_uno - numero_dos
    multiplicacion = numero_uno * numero_dos
    if numero_dos != 0:
        division = numero_uno / numero_dos
    else:
        division = "No se puede dividir por cero"
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}") 
else:
    print("Ambos números deben ser distintos de 0.")

print("")
print("////////////////////////////")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo
#IMC = peso / (altura ** 2). El resultado debe ser un número con dos decimales.
print("ejercicio 8")
print("")
altura = float(input(" ingresa tu altura en metros: "))
peso = float(input(" ingresa tu peso en kilos: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

print("")
print("////////////////////////////")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#Fahrenheit = (9/5) * Celsius + 32. El resultado debe ser un número con dos decimales.
print("ejercicio 9")
print("")

celsius = float(input(" ingresa una temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

print("")
print("////////////////////////////")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("ejercicio 10")
print("")
numero_uno = float(input(" ingresa el primer número: "))
numero_dos = float(input(" ingresa el segundo número: "))
numero_tres = float(input(" ingresa el tercer número: "))
promedio = (numero_uno + numero_dos + numero_tres) / 3
print(f"El promedio de los números ingresados es: {promedio:.2f}")

print("")
print("////////////////////////////")

