#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("---Ejercicio 1 ---")
print("")

for i in range(101):
    print(i)

print("")
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

print("---Ejercicio 2 ---")
print("")

flag = True
while flag:
    num = (input("Ingrese un número entero: "))
    if num.isdigit():
        print ("El numero ingresado tiene ", len(str(num))," dígito/s.")
        flag = False
    elif num[0] == '-' and num[1:].isdigit():
        print ("El numero ingresado tiene ", len(str(num))-1," dígito/s.")
        flag = False
    else:
        print("El valor ingresado no es un número entero. Intente de nuevo.")
        continue
print("")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
print("---Ejercicio 3 ---")
print("")
flag = True
amount = 0
while flag:
    num_one = input("Ingrese el primer número entero: ")
    num_two = input("Ingrese el segundo número entero: ")
    if ((num_one[0] =="-" or num_one[0].isdigit()) and (num_one[1:].isdigit() or len(num_one) ==1)) and ((num_two[0] =="-" or num_two[0].isdigit()) and (num_two[1:].isdigit() or len(num_two) ==1)):
        flag = False
        if int(num_one) >= int(num_two):
            for i in range(int(num_two)+1, int(num_one)):
                amount += i
        else:
            for i in range(int(num_one)+1, int(num_two)):
                amount += i
        print("La suma de los números enteros comprendidos entre ", num_one, " y ", num_two, " es: ", amount)
    
    else:
        print("Almenos uno de los valores ingresados no es un número entero. Intente de nuevo.")
        continue
    


print("")
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0
print("---Ejercicio 4 ---")
print("")
amount = 0
flag = True
while flag:
    num = (input("ingrese un numero entero (0 para finalizar): "))
    if not ((num[0] =="-" or num[0].isdigit()) and (num[1:].isdigit() or len(num) ==1)):
        print("El valor ingresado no es un número entero. Intente de nuevo.")
        continue
    num = int(num)
    if num == 0:
        flag = False
    else:
        amount += num
print("El total acumulado es: ", amount)
print("")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("---Ejercicio 5 ---")
print("")
import random
num_random = random.randint(0, 9)
flag = True
attempts = 0
while flag:
    attempts += 1
    num = (input("Adivine el numero aleatorio entre 0 y 9: "))
    if not (num.isdigit() and 0 <= int(num) <= 9):
        print("El valor ingresado no es un número entero entre 0 y 9. Intente de nuevo.")
        continue
    num = int(num)
    if num == num_random:
        flag = False
        print("bien hecho. Adivinaste el número en ", attempts, " intentos.")
    else:
        print("Numero incorrecto, intenta de nuevo.")
print("")
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("---Ejercicio 6 ---")
print("")
print("Números pares entre 0 y 100 en orden decreciente incluyendo los extremos:")
for i in range(100, -1, -2):
    print(i)
print("")
print("Números pares entre 0 y 100 en orden decreciente excluyendo los extremos:")
for i in range(98, 0, -2):
    print(i)
print("")


print("")
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
print("---Ejercicio 7 ---")
print("")
flag = True
while flag:
    num = input("Ingrese un número entero positivo: ")
    if num.isdigit() and int(num) > 0:
        flag = False
    else:
        print("El valor ingresado no es un número entero positivo. Intente de nuevo.")

num = int(num)
amount = 0
for i in range(num):
    amount += i
print("La suma de los numeros entre 0 y ", num, " es: ", amount)
print("")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("---Ejercicio 8 ---")
print("")
count_even = 0
count_odd = 0
count_negative = 0
count_positive = 0

for i in range(100):
    flag = True
    while flag:
        num = input("Ingrese un número entero: ")
        if (num[0] =="-" or num[0].isdigit()) and (num[1:].isdigit() or len(num) ==1):
            flag = False
        else:
            print("El valor ingresado no es un número entero. Intente de nuevo.")
    num = int(num)
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    if num < 0:
        count_negative += 1
    elif num > 0:
        count_positive += 1
    if num == 0:
        print("El número 0 no se considera ni positivo ni negativo.")
print("Cantidad de números pares: ", count_even)
print("Cantidad de números impares: ", count_odd)
print("Cantidad de números negativos: ", count_negative)
print("Cantidad de números positivos: ", count_positive)
print("")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
print("---Ejercicio 9 ---")
print("")
amount = 0
quantity=100
for i in range(quantity):
    flag = True  
    while flag:
        num = input("Ingrese un número entero: ")
        if (num[0] =="-" or num[0].isdigit()) and (num[1:].isdigit() or len(num) ==1):
            flag = False
        else:
            print("El valor ingresado no es un número entero. Intente de nuevo.")
    num = int(num)
    amount += num
print("La media de los ", quantity, " números ingresados es: ", amount/quantity)
print("")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("---Ejercicio 10 ---")
print("")
flag = True
while flag:
    num = input("Ingrese un número entero: ")
    if (num[0] =="-" or num[0].isdigit()) and (num[1:].isdigit() or len(num) ==1):
        flag = False
    else:
        print("El valor ingresado no es un número entero. Intente de nuevo.")
num_len = len(num)
reversed_num = ""
for i in range(-1, -num_len-1, -1):
    if num[i] == '-':
        continue
    reversed_num += num[i]
reversed_num = int(reversed_num)
num = int(num)
if num < 0:
    reversed_num = reversed_num * -1
print("El numero invertido es: ", reversed_num)
print("")